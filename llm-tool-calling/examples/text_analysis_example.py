"""
Example: Text Analysis with Tool Calling
This example shows how to use text analysis tools with various types of content.
"""

import sys
import os
sys.path.append('../tools')

try:
    from custom_tools import TextAnalysisTool, execute_tool
except ImportError:
    print("Warning: Could not import custom_tools. Running in standalone mode.")
    
    class TextAnalysisTool:
        @staticmethod
        def count_words(text):
            return len(text.split())
        
        @staticmethod
        def count_characters(text, include_spaces=True):
            return len(text) if include_spaces else len(text.replace(' ', ''))
        
        @staticmethod
        def extract_keywords(text, max_keywords=10):
            common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
            words = text.lower().split()
            keywords = [word.strip('.,!?;:"()[]') for word in words if word.lower() not in common_words and len(word) > 2]
            word_freq = {}
            for word in keywords:
                word_freq[word] = word_freq.get(word, 0) + 1
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            return [word for word, freq in sorted_words[:max_keywords]]

def text_analysis_examples():
    """Run various text analysis examples"""
    
    print("📝 Text Analysis Tool Examples")
    print("=" * 35)
    
    # Sample texts for analysis
    texts = {
        "Tech Article": """
        Artificial Intelligence and Machine Learning are transforming the technology landscape. 
        Deep learning algorithms enable computers to process natural language and recognize patterns 
        in complex datasets. These technologies are being applied in healthcare, finance, and 
        autonomous vehicles to solve real-world problems.
        """,
        
        "Business Report": """
        The quarterly financial results show strong growth in revenue and market expansion. 
        Digital transformation initiatives have improved operational efficiency and customer 
        satisfaction. Investment in research and development continues to drive innovation 
        and competitive advantage in emerging markets.
        """,
        
        "Scientific Abstract": """
        This study investigates the effects of climate change on biodiversity conservation 
        in tropical ecosystems. Using statistical modeling and field observations, we analyzed 
        species distribution patterns and habitat fragmentation. The results indicate significant 
        correlations between temperature variations and species migration patterns.
        """
    }
    
    for title, text in texts.items():
        print(f"\n--- {title} ---")
        
        # Basic statistics
        word_count = TextAnalysisTool.count_words(text.strip())
        char_count = TextAnalysisTool.count_characters(text.strip())
        char_count_no_spaces = TextAnalysisTool.count_characters(text.strip(), include_spaces=False)
        
        print(f"Words: {word_count}")
        print(f"Characters (with spaces): {char_count}")
        print(f"Characters (no spaces): {char_count_no_spaces}")
        
        # Extract keywords
        keywords = TextAnalysisTool.extract_keywords(text.strip(), max_keywords=8)
        print(f"Top keywords: {', '.join(keywords[:5])}")
        
        # Calculate reading time (average 200 words per minute)
        reading_time = word_count / 200
        print(f"Estimated reading time: {reading_time:.1f} minutes")
        
        # Text complexity (average word length)
        words = text.strip().split()
        avg_word_length = sum(len(word.strip('.,!?;:"()[]')) for word in words) / len(words)
        print(f"Average word length: {avg_word_length:.1f} characters")
    
    # Comparative analysis
    print(f"\n🔍 Comparative Analysis:")
    print("=" * 25)
    
    all_keywords = []
    for title, text in texts.items():
        keywords = TextAnalysisTool.extract_keywords(text.strip(), max_keywords=3)
        all_keywords.extend(keywords)
        print(f"{title} top keywords: {', '.join(keywords)}")
    
    # Find common themes
    keyword_freq = {}
    for keyword in all_keywords:
        keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
    
    common_keywords = [k for k, v in keyword_freq.items() if v > 1]
    if common_keywords:
        print(f"Common themes across texts: {', '.join(common_keywords)}")
    else:
        print("No common themes found across texts")

def interactive_text_analysis():
    """Interactive text analysis session"""
    
    print(f"\n🎮 Interactive Text Analysis")
    print("=" * 30)
    print("Enter text to analyze (or 'quit' to exit):")
    
    # For demo purposes, analyze a predefined text
    sample_text = input("Enter your text (or press Enter for sample): ").strip()
    
    if not sample_text:
        sample_text = """
        Natural Language Processing enables computers to understand and generate human language. 
        It combines computational linguistics with machine learning to process text and speech data. 
        Applications include chatbots, translation services, sentiment analysis, and document summarization.
        """
        print(f"Using sample text: {sample_text[:100]}...")
    
    if sample_text.lower() != 'quit':
        print(f"\n📊 Analysis Results:")
        
        # Comprehensive analysis
        analysis = {
            "word_count": TextAnalysisTool.count_words(sample_text),
            "character_count": TextAnalysisTool.count_characters(sample_text),
            "keywords": TextAnalysisTool.extract_keywords(sample_text, 10)
        }
        
        print(f"Words: {analysis['word_count']}")
        print(f"Characters: {analysis['character_count']}")
        print(f"Keywords: {', '.join(analysis['keywords'][:5])}")
        
        # Additional metrics
        sentences = sample_text.count('.') + sample_text.count('!') + sample_text.count('?')
        avg_words_per_sentence = analysis['word_count'] / max(sentences, 1)
        print(f"Estimated sentences: {sentences}")
        print(f"Average words per sentence: {avg_words_per_sentence:.1f}")

if __name__ == "__main__":
    text_analysis_examples()
    interactive_text_analysis()
