using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shared.Models.DiscussionForum;

namespace Server.Data.Config;

public class CommentConfig : IEntityTypeConfiguration<Comment>
{
    public void Configure(EntityTypeBuilder<Comment> builder)
    {
        builder.ToTable("Comments");

        builder.HasKey(c => c.CommentId);

        builder.Property(c => c.CommentId)
            .HasColumnName("CommentId")
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

        builder.Property(c => c.PostId)
            .HasColumnName("PostId")
            .IsRequired();

        builder.Ignore(c => c.Post);
    }
}