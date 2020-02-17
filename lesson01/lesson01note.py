Word2Vec Tutorial - The Skip-Gram Model
http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/
包括：
    skip gram neural network Model
目的：
    get into more of the details, skip over the usual introductory and abstract insights about Word2Vec


The Model
如何得到词向量？
    通过训练一个单隐藏层的简单神经网络（目的并不是完成我们的最终任务）

    （类似于无监督学习，数据输入->编码过程->解码过程,简单训练后，将解码过程剥离，可以实现“学习良好图像特征而无需标记训练数据的技巧”？）


The Fake Task（指的上面提到的训练词向量的神经网络，后文简称词向量网络）
如何训练这个词向量网络？
    一个句子，选正中间的一个词（“中词”），在中词相邻近的几个词中**随机**的选择一个词，记录它的位置。
    算出**所有**词出现在这个位置的概率。

    When I say "nearby", there is actually a "window size" parameter to the algorithm. A typical window size might be 5, meaning 5 words behind and 5 words ahead (10 in total).
    
Model Details
So how is this all represented?
    10000个不同词的训练文本，通过one-hot对每个词进行编码，通过一个隐藏层，在来一个输出层（输出也为独热编码）

The Hidden Layer
    隐藏层的参数用10000*300的矩阵表示（google news database 300结果最好）
    训练完成，用每个词的独热编码转置（1 * 10000）乘隐藏层参数即得到1*300的向量（即各自的词向量）。

The Output Layer
    为什么1*300的向量可以代表一个词的词向量？
    因为算法设置这个1*300的向量将在输出层解码（softmax）为1*10000的原独热编码向量，所以证明这个1*300的向量可以代表这个特定的词。
    （输出层参数为300*10000）
两个词有相似语义怎么办？
    如“intelligent” and “smart”，“ant” and “ants” 
    不用怕，我们能干的小网络也会自动为我们学习他们之间细腻的区别的！

空间问题
    隐藏层和输出层都要用300*10000 = 3 *10^6 Byte 即3M空间
    这对大数据集训练是不可接受的，所以word2Vec对其有了一定改进
