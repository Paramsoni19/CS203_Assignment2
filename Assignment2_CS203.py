import numpy as np
import matplotlib.pyplot as plt

def calculate_N(p):
    if p == 1:
        return 367
    if p == 0:
        return 1
    elif p == 0:
        return 1
    else:
        return int(np.ceil(np.sqrt(2 * 365 * np.log(1 / (1 - p)))))


def make_plot(p, output_filename='Birthday_paradox.svg', use_log_scale=False):
    N = calculate_N(p)
    n = np.arange(float(N))
    pbar = np.exp(-n * (n - 1) / (2.0 * 365.0))
    p = 1.0 - pbar

    n05 = 0.5 * (1.0 + np.sqrt(1 - 8.0 * 365.0 * np.log(1.0 - 0.5)))
    plt.plot([n05, n05], [0.0, 0.5], c='k', linestyle='--')
    plt.plot([0.0, n05], [0.5, 0.5], c='k', linestyle='--')
    plt.text(23.5, 0.02, ' ~23')
    plt.plot(n, p, c='r', label='Probability of a pair')
    plt.plot(n, pbar, c='b', label='Probability of no matching pair')

    plt.legend(loc='right')
    plt.xlim(0, N)
    if use_log_scale:
        plt.ylim(1e-6, 1)
        ax = plt.gca()
        ax.set_yscale('log')
    else:
        plt.ylim(0, 1)
        plt.yticks([0.0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0])
    plt.xticks(range(0, N, 10))
    plt.grid(True, ls='-', c='#a0a0a0')
    plt.xlabel('Number of people')
    plt.ylabel('Probability')
    plt.savefig(output_filename)
    plt.show()
    
    return N

# Ask for the value of p
p_value = float(input("Enter the value of p: "))
N_value = make_plot(p_value, output_filename='Birthday_paradox.svg')
print("The value of N is:", N_value)
