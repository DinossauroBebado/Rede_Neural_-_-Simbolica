

import matplotlib.pyplot as plt


def ploter(y_test_scaled, predictions, epoc, batch, dias):
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_facecolor('#858585')
    ax.plot(y_test_scaled, color='red', label='Contaminações real')
    plt.plot(predictions, color='green', label='Contaminações previsão')
    plt.title(
        f"Previsão só com os contaminados\ndias:{dias}, epochs:{epoc}, batch_size:{batch} ")
    plt.legend()
    """plt.show(
    )"""
    plt.savefig(
        f"Neo_Previsão_so_contaminados_dias_{dias}_epochs_{epoc}_batch_size_{batch}.png")
