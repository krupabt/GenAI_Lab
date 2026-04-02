import gensim.downloader as api
import random

# Load pre-trained word vectors
print("Loading word vectors...")
word_vectors = api.load("glove-wiki-gigaword-50")


def get_similar_words(word, top_n=3):
    """Retrieve similar words using word embeddings"""
    try:
        similar_words = word_vectors.most_similar(word, topn=top_n)
        return [w[0] for w in similar_words]
    except KeyError:
        return []


def enrich_prompt(prompt):
    """Replace key words in the prompt with similar words"""
    words = prompt.split()
    enriched_words = []

    for word in words:
        similar_words = get_similar_words(word.lower())
        if similar_words:
            enriched_words.append(random.choice(similar_words))
        else:
            enriched_words.append(word)

    return " ".join(enriched_words)


def generate_simple_story(prompt):
    """Generate a simple story without using OpenAI API"""
    story_templates = [
        f"{prompt} The battle was intense, but courage helped the hero win.",
        f"{prompt} After a long struggle, the hero defeated the enemy and saved the kingdom.",
        f"{prompt} In the end, bravery and determination led to victory."
    ]
    return random.choice(story_templates)


# Example prompt
original_prompt = "Write a short story about a brave warrior fighting a dragon."

# Enrich the prompt
enriched_prompt = enrich_prompt(original_prompt)

# Generate responses
original_response = generate_simple_story(original_prompt)
enriched_response = generate_simple_story(enriched_prompt)

# Print results
print("\nOriginal Prompt:")
print(original_prompt)

print("\nEnriched Prompt:")
print(enriched_prompt)

print("\nGenerated Response for Original Prompt:")
print(original_response)

print("\nGenerated Response for Enriched Prompt:")
print(enriched_response)