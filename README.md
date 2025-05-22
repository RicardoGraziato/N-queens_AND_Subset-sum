# Resumo:
Exercício avaliativo da cadeira de "Projeto e Otimização de Algoritmos" sobre a resolução do problema de "n-rainhas" e do problema de "Soma dos Subconjuntos" utilizando backtracking.

# Problema das N-rainhas

![n-rainhas](https://github.com/user-attachments/assets/50a589fb-538b-49ac-acdf-d13c69c52425)

O problema das N-rainhas consiste em encontrar uma combinação possível de N rainhas num tabuleiro de dimensão N por N tal que nenhuma das rainhas ataque qualquer outra. Duas rainhas atacam-se uma à outra quando estão na mesma linha, na mesma coluna ou na mesma diagonal do tabuleiro. Na figura que se segue pode ver-se as posições atacadas por uma rainha colocada num tabuleiro de dimensão 7 por 7 e ao lado uma possível solução para esse mesmo tabuleiro.

1. Desenvolver uma aplicação que resolva o problema das n-rainhas, encontrando uma solução válida para o problema. Como entrada, o programa recebe um valor para n >= 2, e retorna a disposição das rainhas no tabuleiro.
2. Qual a complexidade da sua solução?
3. Ajuste sua solução para que usar backtracking (se não foi o caso) e para que retorne todas as soluções, não só a primeira.



#

# Problema da Soma dos Subconjuntos

O problema da soma dos subconjuntos é um problema de ciência da computação que 
consiste em verificar se, dado um conjunto de inteiros, existe um subconjunto não-vazio cuja soma é zero. 

Por exemplo, no conjunto {−7, −3, −2, 5, 8}, a resposta é sim, pois o subconjunto {−3, −2, 5} resulta em uma soma de zero. 

1. Faça um método que recebe um conjunto de inteiros e retorna um subconjunto cuja soma seja zero;
2. Altere o método para que retorne todos subconjuntos cuja soma seja zero;
3. Analise a complexidade de ambas as soluções.
