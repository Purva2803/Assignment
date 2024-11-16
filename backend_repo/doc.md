# Posts API Documentation

## Endpoint Overview

The API provides access to posts and their associated comments with built-in pagination support.

### Base URL

```

http://127.0.0.1:8000/api/posts/

```

### Endpoints

#### List Posts

- **URL:** `/api/posts/`
- **Method:** GET
- **Description:** Returns a paginated list of posts with their associated comments

#### Response Format

```json
{
  "count": 35, // Total number of posts
  "next": "http://127.0.0.1:8000/api/posts/?page=2", // URL for next page
  "previous": null, // URL for previous page (null if on first page)
  "results": [
    // Array of post objects
    {
      "id": "uuid-string",
      "text": "Post content",
      "timestamp": "2024-03-14T12:00:00Z",
      "user": {
        "username": "author_username"
      },
      "comments": [
        // Latest 3 comments
        {
          "text": "Comment content",
          "timestamp": "2024-03-14T12:01:00Z",
          "user": {
            "username": "commenter_username"
          }
        }
        // ... up to 3 comments
      ],
      "comment_count": 5 // Total number of comments for this post
    }
    // ... more posts
  ]
}
```

### Pagination

- Default page size: 10 posts per page
- Navigate through pages using the `page` query parameter
- Example:
  ```
  /api/posts/?page=2  // Get second page
  /api/posts/?page=3  // Get third page
  ```
- Use the `next` and `previous` URLs provided in the response for navigation

### Features

- Posts are ordered by timestamp (newest first)
- Each post includes:
  - Unique ID
  - Post text
  - Creation timestamp
  - Author username
  - Up to 3 most recent comments
  - Total comment count
- Comments include:
  - Comment text
  - Creation timestamp
  - Commenter username

### Example Usage

```bash
# Get first page of posts
curl http://127.0.0.1:8000/api/posts/

# Get specific page
curl http://127.0.0.1:8000/api/posts/?page=2

# Get last page (if total posts = 35, last page is 4)
curl http://127.0.0.1:8000/api/posts/?page=4
```

### Implementation Notes

- The endpoint is read-only (GET requests only)
- Timestamps are in ISO-8601 format
- IDs are UUIDs
- Comments are limited to 3 per post in the response
- Infinite scrolling can be implemented using the `next` URL provided in the response
