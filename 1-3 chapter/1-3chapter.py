# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Katya = Character('Катя', color="#c8ffc8")

define StoryTeller = Character('История', color="#c8ffc8")

#персы
image Katya:
   "ch/Легкая улыбка солнце_pixian_ai.png"
   zoom 1

image Katya_Phone:
    "ch/with_phone.png"
    zoom 1.3

image Katya_Macbook:
    "ch/withMacBook.png"
    zoom 1.4

image Katya_Taxi:
    "ch/Katya_Taxi.png"
    zoom 0.7

image Katya_University:
    "ch/Adventure_Start.png"
    zoom 0.8


#фоны

image home_1:
    "bg/Комната Кати с утра.png"
    zoom 2

image taxi:
    "bg/taxi.png"
    zoom 1.6
image university:
    "bg/university.png"
    zoom 1.6

# Игра начинается здесь:
label start:

#Глава 1
label home:
    scene home_1

    StoryTeller "Ясное утро, ознаменовало начало новой главы в жизни Кати"

    show Katya at center
    with dissolve

    StoryTeller "Ясноглазая, амбициозная девушка только что получила сообщение, которое она так долго ждала"
    hide Katya

    show Katya_Phone:
        xalign -3 yalign 0.5
    with dissolve

    StoryTeller "Ее руки дрожали, когда она держала телефон с открытым на нём сообщением от Приёмной комиссии ИРИТ-РТФ УрФУ, престижного университета, известного своей передовой программой в области информационных технологий."
    StoryTeller "Её глаза быстро пробежали по строчкам сообщения, и широкая улыбка расплылась по ее лицу."
    StoryTeller "Она добилась своего, ее приняли."
    StoryTeller "Волнение бурлило в душе Кати, когда она поспешила поделиться новостью со своей семьей."
    StoryTeller "Ее родители, которые с нетерпением ждали, увидели радость в ее глазах еще до того, как она заговорила."
    hide Katya_Phone


    show Katya at center
    with dissolve

    Katya "Мама, папа, я сделала это! - воскликнула она, держа в руках телефон."

    StoryTeller "Родители обняли ее, их лица светились гордостью. \"Мы знали, что ты сможешь это сделать, Катя! Мы так гордимся тобой!\" - сказала ее мать сдавленным от волнения голосом"
    StoryTeller "Ее отец, немногословный человек, просто похлопал ее по плечу с гордой улыбкой."
    hide Katya

    show Katya_Macbook
    with dissolve

    StoryTeller "Затем Катя поделилась новостью со своими лучшими подругами Сашей и Машей. \"Ребята, я поступила!\" - объявила она по видеосвязи. Их реакция была бесценна"
    StoryTeller "Саша кричала от волнения, а у Маши на глазах были слезы."
    StoryTeller "\"О, Катя, это невероятно. Мы знали, что у тебя получится!\" Сказала Саша, широко улыбаясь. Маша, всегда эмоциональная, добавила: \"Я так горжусь тобой, Катя. У тебя все получится\"."
    StoryTeller "Упаковка ее чемоданов была горько-сладким переживанием. Она была взволнована новым путешествием, в которое собиралась отправиться, но в то же время опечалена тем, что оставляет свою семью и друзей позади."
    StoryTeller "Упаковывая свои любимые книги, одежду и фотографии, она поняла, что упаковывает не только свои вещи, но и воспоминания о своей жизни до сих пор."
    StoryTeller "Она пообещала себе, что максимально воспользуется этой возможностью и создаст новые воспоминания, которыми будет дорожить вечно."
    StoryTeller "Застегивая молнию на чемодане и в последний раз оглядывая свою комнату, она почувствовала смесь возбуждения и нервозности. Но в глубине души она знала, что готова к этому новому приключению."

    hide Katya_Macbook

    scene taxi
    show Katya_Taxi:
        xpos -400
        ypos -150
    with dissolve

    StoryTeller "Помахав на прощание родителям и друзьям, она села в машину, которая должна была отвезти ее в аэропорт, готовая начать свою жизнь заново в ИРИТ-РТФ УрФУ."
    hide Katya_Taxi
    scene university
    
    show Katya_University:
        xpos 300
        ypos 120
    with dissolve

    StoryTeller "Ее путешествие только началось"

    #------------- 2 глава

label Part_2:

    scene universityRoom
    #15
    StoryTeller "Катя, молодая девушка с ясными глазами, входит в свою новую комнату в общежитии. Это уютное помещение с двумя двухъярусными кроватями у стены, общим письменным столом, плакатами и картинами, украшающими стены."
    StoryTeller "Катя ставит свои сумки на землю и делает глубокий вдох, впитывая новую обстановку."

    #16
    StoryTeller "Когда она начинает распаковывать вещи, дверь распахивается, открывая двух ее новых соседок по комнате, Нина и Женя."
    show Katya_Surprised:
        xpos -200
        ypos 120
    with dissolve
    
    show Nina:
        xpos 1000
        ypos 160
    with dissolve
    
    show Jenya:
        xpos 400
        ypos 120
    with dissolve

    StoryTeller "Нина, кудрявая девушка с заразительной улыбкой, подбегает к Кате, возбужденно рассказывая об университете и жизни в общежитии."
    hide Nina
    hide Jenya
    hide Katya_Surprised
    #17
    show Nina_Happy:
        xpos 400
        ypos 120
    with dissolve
    Nina "Эй, там! Ты, должно быть, Катя, верно?"
    hide Nina_Happy

    show Nina_Hand:
        xpos 400
        ypos 120
    with dissolve
    #18
    Nina "Я Нина! Я не могу поверить, что мы наконец-то встретились!"
    Nina "Жизнь в общежитии обещает быть такой веселой, а этот университет потрясающий!"
    hide Nina_Hand

    show Katya_Happy:
        xpos 400
        ypos 120
    with dissolve
    #19
    Katya "Да, я Катя. Приятно познакомиться, Нина!"
    Katya "Я тоже очень взволнована. Расскажи мне побольше об университете."
    hide Katya_Happy

    show Nina_Happy:
        xpos 400
        ypos 120
    with dissolve
    #20
    Nina "О, тебе здесь понравится! Занятия отличные, и в университете всегда проходят какие-то мероприятия."

    #21
    Nina " Кроме того, в общежитиях царит фантастическая атмосфера сообщества. Мы будем как маленькая семья!"
    hide Nina_Happy
    StoryTeller "Женя, более отчужденная, но с доброй улыбкой девушка, предлагает Кате помочь с ее багажом. Катя испытывает прилив благодарности и теплоты к этим двум незнакомцам, которые должны стать ее новой семьей."

    #22
    show Jenya:
        xpos 400
        ypos 120
    with dissolve
    Jenya "Привет, я Женя. Помочь с этими сумками?"
    
    #23
    hide Jenya

    show Katya_Happy:
        xpos 400
        ypos 120
    with dissolve
    Katya "О, это было бы здорово, спасибо! Я Катя. Приятно познакомиться с тобой, Женя."

    #24
    hide Katya_Happy

    show Jenya:
        xpos 400
        ypos 120
    with dissolve

    Jenya "Я тоже рада с тобой познакомиться, Катя. Переезд может быть немного ошеломляющим, но мы тебя прикроем. Мы все в этом вместе."
    hide Jenya

    StoryTeller "Затем троица, распаковав вещи, отправляется на экскурсию по обширному университетскому городку."
    StoryTeller "Они проходят мимо ГУК`а, шумного кафетерия и различных учебных корпусов. Катя испытывает чувство благоговения и предвкушения, представляя, какие воспоминания у нее останутся в этих местах."
    
    scene Coridor
    #25
    show Nina_Happy:
        xpos 400
        ypos 120
    with dissolve
    Nina "А это ГУК – Главный Учебный Корпус! Я практически живу здесь во время экзаменов. Поначалу это немного пугает, но ты к этому привыкнешь."

    #26
    hide Nina_Happy
    show Katya_Surprised:
        xpos 400
        ypos 120
    with dissolve

    Katya " Это так впечатляет. Не терпится познакомиться с ним поближе."

    #27
    hide Katya_Surprised

    show Katya_Onigiri:
        xpos 400
        ypos 400
    with dissolve
    show Katya_Onigiri1:
        xpos 600
        ypos 60
    with dissolve
    Jenya "Следующая остановка - оживленный кафетерий. Совет профессионала: бери онигири, не прогадаешь!"

    #28
    Jenya "А это различные учебные корпуса. Ты проведешь здесь много времени, но поверь мне, оно того стоит."

    scene Kovorking
    #29
    show Katya_Happy:
        xpos 400
        ypos 120
    with dissolve
    Katya "Спасибо вам обеим за то, что показали мне окрестности. Я уже могу представить, какие воспоминания у нас останутся в этих местах. Я так благодарна, что вы оба стали соседями по комнате."

    #30
    hide Katya_Happy
    show Nina_Happy:
        xpos 400
        ypos 120
    with dissolve
    Nina "О, Катя, это чувство взаимно. Мы замечательно проведем время вместе!"

    #32
    StoryTeller "На своем первом занятии ее встречает море незнакомых лиц."
    show Katya_Surprised:
        xpos 400
        ypos 120
    with dissolve
    #33
    StoryTeller "Профессор, сурового вида мужчина с седеющими волосами, начинает лекцию, и Катя делает пометки, ее разум охвачен волнением и страхом."

    #34
    StoryTeller "Во время перерыва Катя нервно подходит к группе студентов. Она представляется, и, к ее облегчению, они принимают ее с распростертыми объятиями."
    
    #35
    StoryTeller "Они обмениваются любезностями, немного смеются, и Катя испытывает чувство сопричастности."

    #36
    StoryTeller "Когда день подходит к концу, Катя возвращается в свою комнату в общежитии, усталая, но довольная."

    #37
    StoryTeller "Она делится своими эмоциями с Ниной и Женей, которые охотно слушают, рассказывают свои собственные истории и дают советы."

    #38
    StoryTeller "Той ночью, лежа в своей постели, Катя размышляет о том, как быстро прошел день. Она понимает, что смесь страха и возбуждения, которую она испытывает, является признаком не слабости, а роста"

    #39
    StoryTeller "С этой мыслью она закрывает глаза, готовая встретить лицом к лицу все новые впечатления, которые принесет следующий день. Это было только начало ее новой главы."

        
#------------- 3 глава

label Part_3:
    stop music fadeout 2
    #41 
    scene Kovorking
    play music "chapter3starting.mp3"
    StoryTeller "Катя сидит в коворкинге, углубленно занимаясь программированием. Ее пальцы быстро двигаются по клавиатуре, когда она решает задачи по программированию."
    
    
    show Katya_Macbook
    with dissolve

    #42
    Katya "Капец, как трудно, но мне это нравится."
    StoryTeller "Женя, соседка по комнате Кати и ее однокурсница, подходит и присаживается рядом."

    #43
    hide Katya_Macbook
    show JenyaMackbook:
        xpos 700
        ypos 150
    show Katya_Macbook:
        xpos -150
        ypos -175
    Jenya " Привет, Катя, чем ты здесь так занята?"
    

    #44
    Katya "Привет, Женя. Я просто углубляюсь в учебу, пытаюсь решить эту задачу по программированию. Мне это очень интересно."

    #45
    hide JenyaMackbook
    show Jenya:
        xpos 700
        ypos 0
    Jenya "Да, я знаю, как ты увлечена этим. Мы же обе поступили на программистов. Мне кажется, ты в этом деле будешь просто великолепна."

    #46
    hide Jenya
    hide Katya_Macbook
    show Katya_Happy
    with dissolve
    Katya "Спасибо, Женя. Твои слова мне очень важны."
    
    #47
    hide Katya_Happy
    show Jenya_Looking:
        xpos 250
        ypos 75
    with dissolve
    Jenya "Слушай, Катя, я слышала, что ты начала интересоваться Full-stack разработкой. Это здорово! Я уверена, что ты можешь добиться в этом успеха."

    #48
    hide Jenya_Looking
    show Katya_Look_Forward:
        xpos 275
        ypos -50
    with dissolve
    Katya "Да, я увлечена идеей овладеть всеми аспектами разработки."

    #49
    hide Katya_Look_Forward
    show Jenya:
        xpos 275
        ypos 50
    with dissolve
    Jenya "Мне кажется, неплохо было бы обратиться за помощью к старшекурсницам, которые уже изучают эту область."
    Jenya "Они могут дать тебе ценные советы и указать на полезные ресурсы."

    #50
    hide Jenya
    show Katya_Happy
    Katya "Ты права. Я обязательно поищу кого-нибудь, кто сможет поделиться опытом со мной. Спасибо за совет!"

    #51
    hide Katya_Happy
    StoryTeller "Женя кивает, довольная, что может помочь Кате, и снова устремляет свой взгляд на свою собственную работу."
    
    #52
    scene fon_12
    show Katya_Macbook
    with dissolve
    StoryTeller "Катя находится в компьютерной лаборатории университета, изучая различные аспекты веб-разработки. Она замечает старшекурсницу, которая занята проектом."

    #53
    hide Katya_Macbook
    show Katya_Look_Forward:
        xpos 275
        ypos -50
    with dissolve
    Katya "Простите, не могу ли я задать вам несколько вопросов о том, над чем вы работаете?"

    #54
    hide Katya_Look_Forward
    show Marya
    StoryTeller "Неизвестная обращается к Кате: \"Конечно, рада видеть, что кто-то заинтересован. Ты же первокурсница, как тебя зовут?\" "
    

    #55
    hide Marya
    show Katya_Happy
    Katya "Да, я вот недавно поступила, меня зовут Катя, а тебя?"

    #56
    hide Katya_Happy
    show Marya_Amazed
    Marya " Ооо нифига себе!!!! Меня зовут Мария, приятно познакомиться!"
    hide Marya_Amazed
    StoryTeller "Катя кивает, и они начинают беседу о Full-stack-разработке. Мария объясняет различные концепции и инструменты."

    #57
    show Katya_Happy
    Katya "Расскажи мне, пожалуйста, о Full-stack-разработке"

    #58
    hide Katya_Happy
    show Marya
    Marya "Конечно! Full-stack-разработка - это процесс создания программного обеспечения, где один разработчик работает как с фронтендом, то есть клиентской частью, которую видят пользователи"
    Marya "Так и с бэкендом - серверной частью, которая отвечает за обработку данных."
    Marya "Такой разработчик разбирается во всей технологической цепочке разработки и может работать с различными языками программирования и инструментами."

    #59
    hide Marya
    show Katya_Happy
    Katya "Звучит очень интересно! Какие конкретные инструменты и языки программирования используются при Full-stack-разработке?"

    #60
    hide Katya_Happy
    show Marya
    Marya "Ну, это варьируется в зависимости от проекта и предпочтений разработчика. Но часто используются языки программирования, такие как JavaScript для фронтенда и Python, Ruby или Java для бэкенда."
    Marya "Однако это лишь некоторые примеры, на самом деле есть множество вариантов. Кроме того, мы также используем различные инструменты разработки, такие как фреймворки, библиотеки и системы контроля версий."


    #61
    hide Marya
    show Katya_Surprised
    Katya "Ух ты, так много вещей! Я не могу дождаться, чтобы узнать больше."

    #62
    hide Katya_Surprised
    show Marya_Happy
    Marya "Это увлекательная область с огромными возможностями. Если тебе интересно, я могу порекомендовать тебе несколько ресурсов для начала."

    #63
    hide Marya_Happy
    show Katya_Happy
    Katya "Конечно!"

    #64
    hide Katya_Happy
    show Marya_HappyHappy
    Marya "Я бы порекомендовала тебе начать с онлайн-курсов Ulearn и многие другие, которые вам даёт университет."
    Marya "Они отлично подойдут для начинающих и позволят тебе ознакомиться с основными концепциями и навыками, необходимыми для разработки."
    Marya "Также стоит изучить документацию и примеры проектов, чтобы получить практические навыки."

    #65
    hide Marya_HappyHappy
    show Katya_Look_Forward
    Katya "Спасибо огромное! Я очень благодарна за эти рекомендации. Все это звучит так увлекательно!"

    #66
    hide Katya_Look_Forward
    show Marya_Happy
    Marya "Не за что! Уверена, что тебе понравится. Если у тебя будут еще вопросы или нужна помощь, обращайся ко мне. Я всегда готова помочь новичкам!"

    #67
    hide Marya_Happy
    show Katya_Happy
    Katya "Спасибо, Мария! Я обязательно обращусь, если возникнут вопросы. Пока!"

    #68
    hide Katya_Happy
    show Marya_HappyHappy
    Marya "Пока, Катя! Удачи в изучении Full-stack разработки!"
    hide Marya_HappyHappy
    StoryTeller "Глаза Кати сверкают от волнения, когда она осознала потенциал этой новой области обучения"

    stop music fadeout 2