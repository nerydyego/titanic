from operator import sub

import pandas as pd
        
def submeter_resultados(test, p, arquivo: str ='submission'):
    """
    Cria e salva o arquivo de submissão do Kaggle.

    Parameters
    ----------
    
    test : pd.DataFrame
        Dataset de teste.

    p : array-like
        Predições do modelo.

    arquivo : str
        Nome do arquivo de saída.

    Returns
    -------
    pd.DataFrame
        DataFrame de submissão.
    """
    sub = pd.DataFrame({'PassengerId': test['PassengerId'], 'Survived': p})
    caminho = f'../submission/{arquivo}.csv'
    sub.to_csv(caminho, header=True, index=False)
    print(f'Arquivo de submissão salvo em: {caminho}')
    return sub