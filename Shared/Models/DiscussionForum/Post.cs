namespace Shared.Models.DiscussionForum;

public class Post : Entry
{
    public int PostId { get; set; }
    public string Title { get; set; } = string.Empty;
}