#  要开发一个自动识别谱子的吉他模拟器，达到录入谱即可按照谱发声的效果。
# 除了发声设备外（假设已完成），最重要的就是读谱和译谱能力了。
# 分析其需求，整个过程大致上分可以分为两部分：根据规则翻译谱的内容；根据翻译的内容演奏。
# 我们用一个解释器模型来完成这个功能。


class PlayContext():
    def __init__(self, context):
        self.play_context = context

    @property
    def context(self):
        return self.play_context


class Expression():
    def interpret(self, context):
        if len(context.context) == 0:
            return
        else:
            segs = context.context.split(" ")
            for seg in segs:
                pos = 0
                for ele in seg:
                    if ele.isalpha():
                        pos += 1
                        continue
                    break
                chord = seg[0:pos]
                value = seg[pos:]
                self.execute(chord, value)

    def execute(self, chord, value):
        pass


class Guitar(Expression):
    def execute(self, chord, value):
        print("Normal Guitar Playing--Chord:%s Play Tune:%s" % (chord, value))


if __name__ == "__main__":
    guitar = Guitar()

    context = PlayContext("C53231323 Em43231323 F43231323 G63231323")

    guitar.interpret(context)
