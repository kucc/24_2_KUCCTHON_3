define ch_girl = Character('슈-알루하’타나', color="#c8ffc8")

define ch_unknown = Character('???', color="#c8ffc8")

define ch_main = Character("[player_name]", color="#00aaff")

image img_girl normal:

    im.FactorScale("character/girl/heroine_normal.png",0.5)

    yalign 0.0

image img_girl disgust:

    im.FactorScale("character/girl/heroine_disgust.png",0.5)

    yalign 0.0

image img_girl happy:

    im.FactorScale("character/girl/heroine_happy.png",0.5)

    yalign 0.0

image img_girl sad:

    im.FactorScale("character/girl/heroine_sad.png",0.5)

    yalign 0.0

image img_girl scarynormal:

    im.FactorScale("character/girl/heroine_scarynormal.png",0.5)

    yalign 0.0

image img_girl smile:

    im.FactorScale("character/girl/heroine_smile.png",0.5)

    yalign 0.0

image img_girl scarysmile:

    im.FactorScale("character/girl/heroine_scarysmile.png",0.5)

    yalign 0.0

image bg_normal = "background/normal.png"

image bg_mad = "background/mad.png"

label start:

    $ point = 0

    $ player_name = renpy.input("당신의 이름은 무엇인가요?")

    $ player_name = player_name.strip()

    scene bg_normal with fade

    ch_main "―――「이 넓은 우주에서 오직 지구만이 생명의 구역이라면 공간의 낭비가 아닌가?」"

    "저명한 천체물리학자인 칼 세이건의 어록 중 하나이다. 21세기인 지금까지도, 놀랍게도 인류는 외계 생명과 조우한 적이 없다."

    "외계인과 오컬트에 푹 빠져있던 나는 이 어록을 항상 말버릇처럼 인용하며, 외계인의 존재를 부정하는 자들을 논리적으로 반박하기 위해 노력했다."

    "......당연히, 성인이 되어 철이 든 지금은, 외계인의 존재를 그리 진지하게 확신하지는 않는다."

    "‘만약 외계인이 있었다면, 진작 인류는 멸망했겠지’라는 생각이 언젠가부터 떠오르기 시작했기 때문이다."

    "가끔은 고교 시절의 내가 그립다. 비록 허황된 음모론에 매료되어 벌인 행각일지라도, 그 시절의 나는 ‘무언가에 열중할 수 있는’ 사람이었다."

    "―――지금의 나는 그 때의 열정을 잃었다. 어느 무엇도 나의 흥미를 끌지 않으며, 나는 더이상 아무것도 도전하고 싶지 않다."

    "연이은 실패로 인한 무기력과 우울인 것은 짐작이 간다. 교우 관계에서의 실패, 학업에서의 실패, 자식으로서의 실패, 이성 관계에서의 실패......"

    "――――――’잉여 인간’이라는 호칭이 참으로 걸맞는 사람이다."

    ch_main "「어디서 객사하더라도 아무도 신경쓰지 않을 것 같은 인생인걸....... 뭐, 죽기 전에 외계인의 지구 침략을 막는 업적이라도 세워야 팔자가 좀 달라지려나.」"

    "쓴웃음을 지으며 매일같이 걸어가는 주택가를 거닐었다. 항상 똑같은 풍경, 똑같은 공기, 똑같은, 사람......?"

    ch_main "「...?」"

    show img_girl normal with dissolve

    "누가 봐도 이상한 실루엣이 길거리에 서있었다. 살면서 단 한 번도 본 적 없는 백발, 그리고 붉은 눈을 가진 소녀."

    "머리띠인지, 장식인지는 모르겠으나 천사의 날개 같은 것이 머리에 달려있었다."

    "그제서야 소녀의 옷차림이 눈에 들어왔다. 11월 초순, 슬슬 추위가 몰려올 시기임에도 엉망진창으로 찢어진 거적대기를 대충 걸치고 서있었다."

    "그러나 소녀는 나의 당황스러운 시선에도 불구하고 붉은 눈으로, 나를 지긋이 응시할 뿐이었다."

    ch_main "「저기, 혹시...」"

    show img_girl smile with dissolve

    ch_unknown "「의미 있게 살다가 죽고 싶은거지?」"

    "수십분 전에 내가 한 생각을 전부 꿰뚫어보고 있기라도 한 듯, 소녀는 생글생글 웃으며 내게 물음을 던져왔다."

    ch_unknown "「나, 앞으로 72시간 내에 이 행성을 없애야 하거든. 근데 변덕을 부리고 싶었어. 72시간 동안, 나랑 놀아주지 않을래? 그럼 생각이 바뀔지도 몰라.」"

    "―――이게 무슨 말이지? 뇌가 사고를 정지한 듯, 아무 단어도 머릿속에 들어오지 않았다. 행성을 없애? 72시간? 생각이 바뀌어?"

    "확실히, 소녀의 외양은 인간의 것이 아니었지만, 이렇게 외계의 존재를 조우하게 될 줄은 몰랐다. 애초에 이 녀석은 언제부터 나를 지켜본 것일까."

    ch_main "「......」"

    "당연히 나는 아무 대답도 할 수 없었다. "

    show img_girl happy with dissolve

    ch_unknown "「아―! 나, 이거 알아. 소심한 인간들은 침묵을 동의의 뜻으로 사용한다고 하더라고? 맞지? 맞지, 맞지?」"

    ch_main "「아니, 꼭 그렇지는――」"

    ch_girl "「내 이름은 슈-알루하’타나. 타나라고 불러줘. 지구 시간으로 3일 동안, 날 잔뜩 신나게 해줘. 그럼 잘 부탁해.」"

    hide img_girl normal with dissolve

    "발랄한 목소리로 말을 건네고서는, 소녀는 시야에서 금세 사라졌다. "

    ch_main "「.......................................................」"

    "헛것이겠지? 제발 헛것이었으면 한다."

    "아침. 아침은 내가 가장 좋아하는 시간이다. 시끄러운 도시의 소음도, 사람들의 말 소리도 들리지 않는 가장 개인적이고 고요한―――"

    show img_girl normal with dissolve

    ch_girl "「일―어―나―!」"

    "방에 울려퍼지는 앳된 소녀의 목소리. 저절로 얼굴을 찡그리며 일어나게 되었다."

    "어제의 일이 꿈이 아니었다는 사실이 가장 절망적이다. 나는 잔뜩 잠긴 목소리로 이불 속에서 웅얼거렸다."

    ch_main "「아, 제발....... 아침에는 좀 내버려두라고.」"

    ch_girl "「[player_name]! 나랑 72시간 동안 놀아주기로 했었잖아. 설마 잊어버린거야?」"

   

    menu:

        "1. 너무 졸리고 귀찮지만…… 약속은 약속이니까. 침대에서 일어나 타나와 시간을 보낸다.":

            call wake_up

        "2. 나는 더 자야겠다.":

            call sleep

    show img_girl normal with dissolve

    ch_girl "「………그래서, 타나는 지구에 오게 된 거고, 우주선은 길 건너편 숲 속에 숨겨놨어.」"

    ch_main "「나는 우주선 같은 게 우리 동네로 날아오는 걸 본 적이 없는데?!」"

    ch_girl "「뭐어… [player_name]은 평범한 인간이니까 못 보는 게 당연해.」"

    ch_girl "「그래도 말야, 역시 첫 행성 침공이라서 그런지 중력 때문에 착륙은 아직 어렵더라고. 그래서 우주선 안에 있던 물건들이 잔~뜩 쏟아져나온 상태긴 해. 헤헤, 에헤헤……」"

    ch_main "「…고치지 않아도 되는거야?」"

    ch_girl "「아직은 지구를 부숴버릴 마음이 들진 않으니까.」"

    ch_main "「섬뜩하네…」"

    ch_girl "「아앗―! 방금 ‘섬뜩하다’고 말했지? 역시 이런 외형이어도 인간에게 공포감을 유발하는구나. 그치, 그치?」"

    "타나는 눈을 반짝이며 나를 바라보았다. ……내가 여기서 무슨 대답을 해야 타나의 심기를 건드리지 않을 수 있을까."

    menu:

        "1. 하나도 안 무섭다고 말하며 비꼰다.":

            call mean

        "2. 어린 아이를 달래듯… 비위에 맞춰준다.":

            call kind

    show img_girl normal with dissolve

    ch_main "「이제 24시간밖에 안 남았네, 타나.」"

    ch_girl "「으응.」"

    "소녀는 살짝 아쉬운듯, 머리에 달린 두 날개를 추욱 늘어뜨리며 대답했다."

    "나는 타나의 머리를 느리게 쓰다듬으며 달래주었다. 살면서 만져본 머리카락 중 가장 부드럽고, 좋은 향기가 나는 머리였다."

    "그러자 작은 외계인은 날 올려다보며 중얼거렸다."

    ch_girl "「…타나랑 보낸 시간은 어땠어? 행복했어? 싫었어?」"

    menu:

        "1. 행복했다고 말한다.":

            call happy

        "2. 지구 침공하는 외계인이랑 하는 3일간의 동거가 어떻게 행복하냐? 별로였다고 말한다.":

            call bad

    "D-DAY"

    "약속의 72시간이 지났다. 아침에 일어나보니 타나는 없었다. 이미 지구 침공을 시작한 것일까? 아니면 고향으로 돌아간 것일까."

    "집안 곳곳을 뒤져보며 작은 외계인을 찾아보았지만, 모습이 보이지 않았다."

    ch_main "「………」"

    "불안해하던 찰나, 타나가 이전에 해주었던 말이 뇌리에 스쳐지나갔다. 분명, ‘우주선을 길 건너편의 숲 속에 숨겨놓았다’라고 말했었지. 나는 공원으로 향했다."

    "얼마나 나뭇가지를 헤치고 깊게 들어갔을까. 숲의 전경과는 전혀 어울리지 않는 거대한 우주선이 놓여있었다."

    if point == 3:

        ch_girl "「[player_name]! 내 말을 잘 기억하고 와주었구나.」"

        ch_main "「타나, 말도 안 하고 숲 속으로 와버리면 어떡해.」"

        ch_girl "「헤헤… 그치만, [player_name]이 스스로 내 우주선 앞에 다다르길 바랐어.」"

        ch_main "「…어째서?」"

        ch_girl "「내가 끌고 온 것도 아닌, 누가 시켜서 온 것도 아닌, [player_name] 스스로의 의지로 내 곁에 와주었다는 뜻이니까.」"

        ch_main "「……무슨 의도인지 모르겠어. 타나, 너 지구 침공은?」"

        ch_girl "「그만두려고. 72시간 동안, [player_name]을 너무 좋아하게 되어서 지구를 없애고 싶지 않아졌어. 헤헤, 물론 고향에 돌아가면 잔뜩 혼나겠지. 솔직히, 살아돌아갈 수 없을거야.」"

        "―타나가 죽지 않도록 하고 싶다. 72시간이라는 짧은 시간동안, 타나는 나의 모든 걸 바꿨다고 말해도 과언이 아닐 정도로 타나는, 나의 삶의 일부가 되어줬다. "

        "타나와 함께 하고 싶다. 타나와 더 많은 것들을 즐기고 싶다. 나는, 나는 타나를……"

        ch_main "「…함께 우주로 가자. 어떻게든 너와 더 이 우주를 살고 싶어.」"

        ch_girl "「!!!!」"

        scene bg_mad with dissolve

        "그렇게 나는 타나와 함께 우주선에 올랐다. 이제, 몰려드는 외계인들을 모두 무찌르고 타나와 행복하게 지낼 일만 남았다…!"


    return

label wake_up:

    ch_main "「알았어, 알았어. ……뭘 하고 놀면 좋을까.」"

    ch_girl "「배가 고파. [player_name]이(가) 주로 가는 식당에 데려다줘.」"

    $ point += 1

    return

label sleep:

    ch_main "「아, 저리가……」"

    show img_girl scarynormal with dissolve

    ch_girl "「………」"

    return

label mean:

    ch_main "「…너 같은 외계인을 보고 놀라는 사람은 아무도 없을걸?」"

    ch_girl "「………」"

    show img_girl scarynormal with dissolve

    return

label kind:

    ch_main "「아너무무서워서사실마주칠때도깜짝놀랐어너같은침략자라면모든인류가벌벌떨거야」"

    show img_girl smile with dissolve

    ch_girl "「하핫. 역시 그렇지?」"

    ch_girl "「그래도말이야, 마냥 무섭기만 하진 않았으면 좋겠는데……」"

    "타나는 얼굴을 붉히며 볼을 긁적거렸다."

    $ point += 1

    return

label happy:

    ch_main "「당황스럽지 않았다고 하면 거짓말이겠지만… 예상과는 정반대로, 타나와 보낸 시간들은 행복했어.」"

    ch_main "「누군가와 이렇게 가까이 지낸 것도 참 오랜만이고, 무엇보다도… 타나는 귀여우니까.」"

    show img_girl happy with dissolve

    ch_girl "「…!」"

    $ point += 1

    return

label sad:

    ch_main "「…어… 솔직히, 즐거울 리가 없지…」"

    show img_girl disgust with dissolve

    ch_girl "「………」"

    return




















