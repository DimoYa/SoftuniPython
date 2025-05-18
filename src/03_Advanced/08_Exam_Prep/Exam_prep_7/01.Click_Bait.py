from collections import deque

suggested_links = deque([int(el) for el in input().split()])
featured_articles  = [int(el) for el in input().split()]
target_value = int(input())
final_feed = []

while suggested_links and featured_articles:
    current_link = suggested_links.popleft()
    current_article = featured_articles.pop()

    greater = max(current_link, current_article)
    smallest = min(current_link, current_article)
    remainder = greater % smallest

    if greater == current_article:
        final_feed.append(remainder)
        if remainder != 0:
            featured_articles.append(remainder *2)
    elif greater == current_link:
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder *2)
    else:
        final_feed.append(0)

print(f"Final Feed: {', '.join([str(el) for el in final_feed])}")

total_eng_value = sum(final_feed)

if total_eng_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_eng_value}")
else:
    print(f"Goal not achieved! Short by: {target_value - total_eng_value}")
