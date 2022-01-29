def teorema_bayes (prob_b_dado_a, prob_a,prob_b):
    return (prob_b_dado_a*prob_a)/prob_b

if __name__ == '__main__':
    prob_cancer = (1/100_000)
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10/99_999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = prob_cancer*prob_sintoma_dado_cancer+prob_sintoma_dado_no_cancer*prob_no_cancer
    
    prob_cancer_dado_sintomas = teorema_bayes(prob_sintoma_dado_cancer,prob_cancer,prob_sintoma)

    print(f'la probabilidad de tener cancer es de: {prob_cancer_dado_sintomas}%')