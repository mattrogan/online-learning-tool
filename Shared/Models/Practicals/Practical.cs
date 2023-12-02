namespace Shared.Models.Practicals;

public class Practical
{
    public int PracticalId;
    public string Description { get; set; } = string.Empty;
    public string WorksheetUrl { get; set; } = string.Empty;
    public string SolutionsUrl { get; set; } = string.Empty;
}