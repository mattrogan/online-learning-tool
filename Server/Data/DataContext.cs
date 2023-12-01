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
    }
}