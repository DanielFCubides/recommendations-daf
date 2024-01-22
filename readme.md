[![codecov](https://codecov.io/github/DanielFCubides/recommendations-daf/graph/badge.svg?token=SY8CJQJFME)](https://codecov.io/github/DanielFCubides/recommendations-daf)

# Recommendation System 

Welcome to the Recommendation System API repository. This system provides recommendations for users based on their preferences and items they might be interested in. The main feature of this API is the ability to calculate a score between a user and an item, helping users discover relevant content.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
## Getting Started

To get started with the Recommendation System API, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/DanielFCubides/recommendations-daf.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API server:

   ```bash
   python app.py
   ```

4. Access the API at `http://localhost:5000` in your web browser or use a tool like [Postman](https://www.postman.com/) for testing.

## Usage

The Recommendation System API allows users to calculate a score between a user and an item, providing personalized recommendations. This score can be used to suggest relevant items to users based on their preferences and behaviors.

## API Endpoints

- **Calculate Score**: Calculate a score between a user and an item.

  - **Endpoint**: `/calculate-score`
  - **HTTP Method**: POST
  - **Request Body**:
    ```json
    {
      "user_id": "user123",
      "item_id": "item456"
    }
    ```
  - **Response**:
    ```json
    {
      "user_id": "user123",
      "item_id": "item456",
      "score": 75
    }
    ```

## Stability
[![codecov](https://codecov.io/github/DanielFCubides/recommendations-daf/graphs/sunburst.svg?token=SY8CJQJFME)](https://codecov.io/github/DanielFCubides/recommendations-daf)


### Strategy

The first recomendation system, the score will be  the maximum prime number between two given numbers and then calculate its modulo 100

[//]: # (## Configuration)

[//]: # ()
[//]: # (Before using the API, you need to configure it by editing the `config.py` file. You can set various parameters, such as database connection details, scoring algorithms, and more.)

[//]: # ()
[//]: # (```python)

[//]: # (# Example configuration in config.py)

[//]: # (DATABASE_URL = "your_database_url_here")

[//]: # (SCORING_ALGORITHM = "your_scoring_algorithm_here")

[//]: # (# Add more configuration options as needed)


[//]: # (## Contributing)

[//]: # ()
[//]: # (We welcome contributions to enhance the Recommendation System API. Feel free to submit issues, propose new features, or make pull requests. Please review our [Contributing Guidelines]&#40;CONTRIBUTING.md&#41; for more details.)

[//]: # ()
[//]: # (## License)

[//]: # ()
[//]: # (This project is licensed under the MIT License. See the [LICENSE]&#40;LICENSE&#41; file for details.)
