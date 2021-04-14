import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def main():

    path = 'C:\\Users\\Steven\\Documents\\Books\\Cixin Liu\\The Dark Forest (81)\\tdf.epub'
    
    book = read_epub(path)
    chapters = epub_to_html(book)

    chapter7 = format_chapters(chapters[7])
    print(chapter7)

def read_epub(epub_path):
    book = epub.read_epub(epub_path)
    return book


def epub_to_html(book):
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

def format_chapters(chapter):
    output = ''
    blacklist = []
    soup = BeautifulSoup(chapter, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output


if __name__ == "__main__":
    main()