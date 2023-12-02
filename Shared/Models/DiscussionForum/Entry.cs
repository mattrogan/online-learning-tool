namespace Shared.Models.DiscussionForum;

public abstract class Entry
{
    public string? Author { get; set; }
    public string Content { get; set; } = string.Empty;
    public DateTime DatePosted { get; set; }
}