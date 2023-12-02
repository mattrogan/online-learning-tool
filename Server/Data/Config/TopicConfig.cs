using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shared.Models.LearningMaterials;

namespace Server.Data.Config
{
    public class TopicConfig : IEntityTypeConfiguration<Topic>
    {
        public void Configure(EntityTypeBuilder<Topic> builder)
        {
            builder.ToTable("Topics");

            builder.HasKey(t => t.TopicId);

            builder.Property(t => t.TopicId)
                .HasColumnName("TopicId")
                .IsRequired();

            builder.Property(t => t.Title)
                .IsRequired();

            builder.Property(t => t.Content)
                .IsRequired();

            builder.Property(t => t.VideoUrl)
                .IsRequired(false);
        }
    }
}