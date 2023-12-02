using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Shared.Models.Practicals;

namespace Server.Data.Config;

public class PracticalConfig : IEntityTypeConfiguration<Practical>
{
    public void Configure(EntityTypeBuilder<Practical> builder)
    {
        // id description worksheet solution
        builder.ToTable("Practicals");

        builder.HasKey(p => p.PracticalId);

        builder.Property(p => p.PracticalId)
            .HasColumnName("PracticalId")
            .IsRequired();

        builder.Property(p => p.Description)
            .HasColumnName("Description")
            .IsRequired();

        builder.Property(p => p.WorksheetUrl)
            .HasColumnName("WorksheetUrl")
            .IsRequired();

        builder.Property(p => p.SolutionsUrl)
            .HasColumnName("SolutionsUrl")
            .IsRequired();
    }
}