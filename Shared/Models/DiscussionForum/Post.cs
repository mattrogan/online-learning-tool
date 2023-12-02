namespace Shared.Models.DiscussionForum;

public class Post : Entry
{
    public Post()
    {
        Comments = new List<Comment>();
    }
    
    public int PostId { get; set; }
    public string Title { get; set; } = string.Empty;
    public IEnumerable<Comment> Comments { get; set; }
}