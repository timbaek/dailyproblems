'''
You are on a flight and wanna watch two movies during this flight.
You are given int[] movie_duration which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

e.g.
Input
movie_duration: [90, 85, 75, 60, 120, 150, 125]
d: 250

Output
[90, 125]
90min + 125min = 215 is the maximum number within 220 (250min - 30min)
'''

def solution(arr, d):
  first, second = 0, 0

  for i in range(0,len(arr)):
    if arr[i] > first:
      if arr[i] + first <= d - 30:
        second = first
        first = arr[i]
      elif arr[i] + second <= d - 30:
        first = arr[i]

    elif arr[i] > second and arr[i] + first <= d - 30:
      second = arr[i]

  return [second, first]

print(solution([90, 85, 75, 60, 120, 150, 125], 250))
print(solution([90, 85, 75, 60, 120, 150, 125], 180))
