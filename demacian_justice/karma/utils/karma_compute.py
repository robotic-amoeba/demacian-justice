from math import sqrt

# Lower bound of Wilson score confidence interval for a Bernoulli parameter
# https://www.evanmiller.org/how-not-to-sort-by-average-rating.html
# https://medium.com/hacking-and-gonzo/how-reddit-ranking-algorithms-work-ef111e33d0d9
def wilson_score(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    # z: 1.44 = 85%, 1.96 = 95%
    z = 1.96
    phat = float(ups) / n
    left = phat + 1/(2*n)*z*z
    right = z*sqrt(phat*(1-phat)/n + z*z/(4*n*n))
    under = 1+1/n*z*z

    lower_bound = (left - right) / under
    return lower_bound
