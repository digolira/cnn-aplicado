DATASET:
https://archive.ics.uci.edu/dataset/920/jute+pest+dataset


Islam, M. (2024). Jute Pest [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5289P.



Instruções:

**Arquivo 1**: imp1_lenet_alexnet.ipynb

Nesse arquivo houve um benchmarking, explorando algumas opções de arquitetura já existentes e que fossem simples de implementar. Foram encontradas duas interessantes que se encaixam nesse propósito:

- LeNet
- AlexNet


**Arquivo 2**: imp2_arquitetura_manual.ipynb

Nesse arquivo houve uma tentativa de desenvolver uma arquitetura de CNN simples, com poucas camadas, e que fosse melhor que as do benchmarking do arquivo 1. 


**Arquivo 3**: imp3_finetunning.ipynb

Nesse arquivo, primeiro se usou transfer learning, se utilizando do modelo pré treinado VGG16, e adicionando uma camada densa ao fim, retreinando o modelo. Posteriormente, houve o descongelamento de 4 (quatro) camadas convolucionais, e retreinamento com fine-tunning.

**Arquivo 4 (opcional)**:  splitting.py

Arquivo de script linux opcional, nesse arquivo é para fazer a divisão da base de fotos em teste, treino e validação.  Basta indicar as pastas que estão os arquivos e a pasta de destino para as divisões. 