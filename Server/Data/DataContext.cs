using Microsoft.EntityFrameworkCore;
using Server.Data.Config;

namespace Server.Data;

public class DataContext : DbContext
{
    public DataContext(DbContextOptions opts)
        : base(opts)
    {
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfiguration(new TopicConfig());
        modelBuilder.ApplyConfiguration(new PostConfig());
        modelBuilder.ApplyConfiguration(new CommentConfig());
        modelBuilder.ApplyConfiguration(new PracticalConfig());
    }
}