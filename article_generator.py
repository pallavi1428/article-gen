import os
from datetime import datetime
import openai
from dotenv import load_dotenv
import sys
from pathlib import Path

# Load environment variables
load_dotenv()

# Initialize OpenAI client with error handling
try:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    print(f"Failed to initialize OpenAI client: {e}")
    sys.exit(1)

def generate_titles(topic: str, num_titles: int = 5) -> list[str]:
    """Generate multiple title options for a given topic."""
    if not topic.strip():
        raise ValueError("Topic cannot be empty")
    
    prompt = f"""Generate {num_titles} compelling article titles about {topic}. 
    Requirements:
    - Attention-grabbing and SEO-friendly
    - Maximum 60 characters each
    - Return just the titles, one per line"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
        )
        titles = [title.strip() for title in response.choices[0].message.content.split('\n') if title.strip()]
        return titles[:num_titles]  # Ensure we return only the requested number
    except Exception as e:
        print(f"Error generating titles: {e}")
        return []

def select_best_title(titles: list[str]) -> str:
    """Let the user select the best title from the generated options."""
    if not titles:
        raise ValueError("No titles provided for selection")
    
    print("\nGenerated Title Options:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")
    
    while True:
        try:
            choice = input("\nSelect the best title (enter number) or 'r' to regenerate: ").strip().lower()
            
            if choice == 'r':
                return None  # Signal to regenerate
                
            choice = int(choice)
            if 1 <= choice <= len(titles):
                return titles[choice-1]
            print(f"Please enter a number between 1 and {len(titles)}")
        except ValueError:
            print("Invalid input. Please enter a number or 'r' to regenerate")

def generate_article(title: str) -> str:
    """Generate a full article based on the selected title."""
    prompt = f"""Write a comprehensive article titled: '{title}'. 
    Requirements:
    - Markdown format with proper headings
    - Include introduction, body, and conclusion
    - Use bullet points where appropriate
    - Minimum 500 words
    - Add section for Key Takeaways at the end"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=2000,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating article: {e}")
        return ""

def save_to_markdown(title: str, content: str, directory: str = "articles") -> Path:
    """Save the generated article to a markdown file."""
    try:
        # Create directory if it doesn't exist
        output_dir = Path(directory)
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # Create filename
        clean_title = "".join(c if c.isalnum() or c in " -_" else "" for c in title)
        filename = f"{clean_title.strip().replace(' ', '_')}.md"
        filepath = output_dir / filename
        
        # Add metadata and save
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            f.write(content)
        
        print(f"\nArticle successfully saved to: {filepath.resolve()}")
        return filepath
    except Exception as e:
        print(f"Error saving file: {e}")
        raise

def main():
    print("🚀 Advanced Article Generator")
    print("----------------------------")
    
    while True:
        # Get topic from user
        topic = input("\nEnter the article topic (or 'q' to quit): ").strip()
        if topic.lower() == 'q':
            break
            
        if not topic:
            print("⚠️ Topic cannot be empty!")
            continue
            
        # Title generation loop
        while True:
            # Step 1: Generate titles
            print("\nGenerating title options...")
            titles = generate_titles(topic)
            if not titles:
                print("Failed to generate titles. Please try again.")
                continue
                
            # Step 2: Select best title
            selected_title = select_best_title(titles)
            if selected_title is None:
                continue  # Regenerate titles
                
            print(f"\n✅ Selected title: {selected_title}")
            
            # Step 3: Generate article
            print("\nGenerating article...")
            article_content = generate_article(selected_title)
            if not article_content:
                print("Failed to generate article. Please try again.")
                continue
                
            # Step 4: Save to markdown
            try:
                save_to_markdown(selected_title, article_content)
                break  # Exit title loop on success
            except:
                print("Please try again")
                
        # Prompt to continue
        if input("\nGenerate another article? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"\n⚠️ An unexpected error occurred: {e}")