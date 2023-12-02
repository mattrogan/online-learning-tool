namespace Shared.Models.DiscussionForum;

public class Comment : Entry
{
    public int CommentId { get; set; }
    public int PostId { get; set; }
    public Post? Post { get; set; }
}