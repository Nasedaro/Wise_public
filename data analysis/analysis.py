from collections import defaultdict
from math import sqrt

# 노인 후기 데이터 (가정)
reviews = [
    {"user_id": 1, "job_id": 101, "job_rating": 4, "age": 68, "gender": "Male", "physical_ability": "Good", "company_rating": 5},
    {"user_id": 2, "job_id": 101, "job_rating": 5, "age": 72, "gender": "Female", "physical_ability": "Good", "company_rating": 4},
    {"user_id": 3, "job_id": 102, "job_rating": 3, "age": 66, "gender": "Male", "physical_ability": "Average", "company_rating": 3},
    # 추가 후기 데이터
]

# 사용자 간 유사도 계산
def calculate_similarity(user1, user2):
    similarity_score = 0

    # 유사도 측정을 위한 각 특성 비교
    if user1['age'] == user2['age']:
        similarity_score += 1
    if user1['gender'] == user2['gender']:
        similarity_score += 1
    if user1['physical_ability'] == user2['physical_ability']:
        similarity_score += 1
    if user1['company_rating'] == user2['company_rating']:
        similarity_score += 1

    return similarity_score

# 유사도를 기반으로 추천
def recommend_job(reviews, target_user):
    user_similarities = defaultdict(int)
    job_ratings = defaultdict(int)
    job_similarity_sums = defaultdict(int)

    for review in reviews:
        similarity = calculate_similarity(target_user, review)
        user_similarities[review['job_id']] += similarity
        job_ratings[review['job_id']] += review['job_rating']
        job_similarity_sums[review['job_id']] += 4  # 최대 유사도 값 (4개의 특성)

    recommended_job = max(user_similarities, key=lambda x: (job_ratings[x] / job_similarity_sums[x]))
    return recommended_job

# 특정 노인을 대상으로 일자리 추천
target_user = {"age": 75, "gender": "Male", "physical_ability": "Good", "company_rating": 4}  # 대상 노인의 특성
recommended_job = recommend_job(reviews, target_user)

print(f"추천된 직무: Job ID {recommended_job}")