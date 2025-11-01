from sentiment_analysis import sentiment_analyzer

def main():
    text = "I love this suit."
    print(f"Analyzing sentiment for: '{text}'\n")

    try:
        result = sentiment_analyzer(text)

        # Check for API or network errors
        if "error" in result:
            print(f"❌ Something went wrong: {result['error']}")
        else:
            print("✅ Analysis result:")
            print(result)

    except Exception as e:
        print(f"⚠️  An unexpected exception occurred: {e}")

if __name__ == "__main__":
    main()
