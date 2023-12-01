using Microsoft.EntityFrameworkCore;

namespace Server.Data;

public class DataContext : DbContext
{
    public DataContext(DbContextOptions opts)
        : base(opts)
    {
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
    }
}