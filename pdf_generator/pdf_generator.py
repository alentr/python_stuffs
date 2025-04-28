import os
import random
import string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
import argparse
from tqdm import tqdm

# to run: 
# 1: pip install reportlab tqdm
# 2: python pdf.py --num_files 5 --num_pages 3

# Lists for generating meaningful filenames
adjectives = ["annual", "quarterly", "strategic", "technical", "financial", "operational", "detailed", 
              "comprehensive", "executive", "internal", "confidential", "preliminary", "advanced", 
              "formal", "digital", "analytical", "corporate", "business", "professional", "scientific"]

nouns = ["report", "analysis", "summary", "proposal", "overview", "review", "assessment", "evaluation", 
         "document", "presentation", "statement", "brief", "plan", "guide", "manual", "handbook", 
         "outline", "strategy", "roadmap", "whitepaper"]

topics = ["project", "market", "research", "performance", "budget", "development", "operations", 
          "growth", "investment", "compliance", "quality", "security", "implementation", "survey", 
          "audit", "forecast", "trends", "initiative", "program", "portfolio"]

def generate_meaningful_filename():
    """Generate a filename with a combination of adjective + noun + topic that makes sense."""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    topic = random.choice(topics)
    
    return f"{adj}_{noun}_{topic}"

def generate_random_text(min_words=50, max_words=200):
    """Generate random text with a random number of words."""
    words = []
    word_count = random.randint(min_words, max_words)
    
    for _ in range(word_count):
        word_length = random.randint(3, 12)
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
        words.append(word)
    
    return ' '.join(words)

def create_random_page(c, page_num):
    """Create a random page with text and some basic elements."""
    c.setFont("Helvetica", 12)
    
    # Add page number
    c.setFont("Helvetica-Bold", 10)
    c.drawString(inch * 7, inch * 0.5, f"Page {page_num}")
    
    # Random header
    c.setFont("Helvetica-Bold", 16)
    header = f"Section {random.randint(1, 10)}.{random.randint(1, 10)}"
    c.drawString(inch, inch * 10, header)
    
    # Random paragraphs
    c.setFont("Helvetica", 12)
    y_position = inch * 9
    
    paragraphs = random.randint(3, 6)
    for _ in range(paragraphs):
        text = generate_random_text()
        
        # Split text into lines to fit page width
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            if len(' '.join(current_line)) > 65:  # Approximate characters per line
                lines.append(' '.join(current_line))
                current_line = []
        
        if current_line:
            lines.append(' '.join(current_line))
            
        # Draw each line
        for line in lines:
            y_position -= 18
            if y_position < inch:  # If we're at the bottom of the page, stop adding text
                break
            c.drawString(inch, y_position, line)
        
        y_position -= 18  # Space between paragraphs
    
    # Maybe add a random shape
    if random.random() > 0.7:
        c.setStrokeColor(random.choice([colors.red, colors.blue, colors.green, colors.black]))
        shape_type = random.choice(['circle', 'rectangle'])
        x = random.uniform(1, 6) * inch
        y = random.uniform(1, 8) * inch
        
        if shape_type == 'circle':
            radius = random.uniform(0.2, 1) * inch
            c.circle(x, y, radius, fill=0)
        else:
            width = random.uniform(0.5, 2) * inch
            height = random.uniform(0.5, 1) * inch
            c.rect(x, y, width, height, fill=0)

def generate_random_pdf(output_dir, file_index, num_pages):
    """Generate a single random PDF with the specified number of pages."""
    # Generate a meaningful filename instead of a sequential number
    base_filename = generate_meaningful_filename()
    filename = f"{base_filename}_{file_index}.pdf"
    filepath = os.path.join(output_dir, filename)
    
    c = canvas.Canvas(filepath, pagesize=letter)
    
    for page_num in range(1, num_pages + 1):
        create_random_page(c, page_num)
        if page_num < num_pages:
            c.showPage()  # Start a new page
    
    c.save()
    return filepath

def main():
    parser = argparse.ArgumentParser(description='Generate random PDF files')
    parser.add_argument('--num_files', type=int, default=5, help='Number of PDF files to generate')
    parser.add_argument('--num_pages', type=int, default=3, help='Number of pages per PDF file')
    parser.add_argument('--output_dir', type=str, default='random_pdfs', help='Output directory')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    print(f"Generating {args.num_files} PDF files with {args.num_pages} pages each...")
    
    for i in tqdm(range(1, args.num_files + 1)):
        filepath = generate_random_pdf(args.output_dir, i, args.num_pages)
    
    print(f"PDF generation complete. Files saved to {os.path.abspath(args.output_dir)}")

if __name__ == "__main__":
    main()
