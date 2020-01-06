# Note
四个模型分别是啥？如何构建？如何训练？

编码模型
记忆模型
策略模型
解码模型

## 常见名词解析

tf.contrib.framework.nest

absl 在哪儿？干啥用的？ flags app logging 函数的入口启动和日志记录。打辅助的。
    
    flags可以帮助我们通过命令行来动态的更改代码中的参数。

    一个demo（节选）：

    from absl import app, flags, logging
     
    flags.DEFINE_string('type', '','input type.')
    flags.DEFINE_integer('index', 0,'input idnex')
     
    FLAGS = flags.FLAGS
     
    print(FLAGS.type)
    print(FLAGS.index)

    在命令行输入

    python test.py  --index=0 --type=ps

    结果：

    ps
    0

batch_size = FLAGS.batch_size #应该有不止一个环境和智能体同时进行训练，默认16个，那么怎么把他们合起来呢？ 为啥把他们合起来


collection 又是个啥？
    collections是Python内建的一个集合模块，提供了许多有用的集合类。
    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> p = Point(1, 2)
    >>> p.x
    1
    >>> p.y
    2
    namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

    这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

    还有Counter，OrderedDict，defaultdict，deque 等


sonnet as snt 是啥：
    Sonnet是基于TensorFlow的一个库，可用于方便地构建复杂的神经网络，git地址为：https://github.com/deepmind/sonnet
    有一些关于mlp cnn lstm 的基础定义

agent 构造：
    初始化的时候有两个基础函数，ImageEncoderDecoder（这个东西里有关于图像的编码解码部分的网络结构，下面的_encode和_decode 用的到）和_RMACore(step 中用到)
    
    _encode 输入是_prepare_observations（其中包含了，observation，last_reward, last_action三部分）
        encode 里用到了_convnet= snt.nets.ConvNet2D（）输出是16*32只是用来编码observation的
        action 是用onehot 编码得到的
        reward是用了一个叫expand_dim 的函数得到的
        features就是把他们三个concat起来

    _decode 也有三部分：
        decode 用来解码图像部分，action reward都是线性解码
        重构的观测recons包括三个部分：image=image_recon，last_reward=reward_recon,last_action=action_recon

    step 输入是_encode 得到的编码feature，????待续




## encoder





