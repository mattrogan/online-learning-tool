using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shared.Models.DiscussionForum;

namespace Server.Data.Config;

public class PostConfig : IEntityTypeConfiguration<Post>
{
    public void Configure(EntityTypeBuilder<Post> builder)
    {
        builder.ToTable("Posts");

        builder.HasKey(p => p.PostId);

        builder.Property(p => p.PostId)
            .HasColumnName("PostId")
            .IsRequired();

        builder.Property(p => p.Title)
            .HasColumnName("Title")
            .IsRequired();

        builder.Property(p => p.Content)
        .HasColumnName("Content")
        .IsRequired();

        builder.Property(p => p.Author)
        .HasColumnName("Author")
        .IsRequired(false);

        builder.Property(p => p.DatePosted)
            .HasColumnName("DatePosted")
            .HasDefaultValue(DateTime.Now)
            .IsRequired();

        builder.HasMany(p => p.Comments)
            .WithOne(c => c.Post)
            .HasPrincipalKey(p => p.PostId)
            .HasForeignKey(c => c.PostId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}