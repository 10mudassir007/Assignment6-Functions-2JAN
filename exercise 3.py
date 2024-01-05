import emoji

def sentiment(text):
    review = emoji.demojize(text)
    review_list = review.split()
    positive =  ['good','excellent','grateful','happy','positive','thankful','satisfied','cheerful','pleased',':glowing_star:','delighted',':grinning_face_with_smiling_eyes:',':grinning_face_with_big_eyes:',':beaming_face_with_smiling_eyes:',':grinning_squinting_face:',':grinning_face_with_sweat:',':face_with_tears_of_joy:',':rolling_on_the_floor_laughing:',':smiling_face_with_smiling_eyes:',':smiling_face_with_sunglasses:',':smiling_face_with_heart-eyes:',':grinning_face_with_big_eyes:']
    neutral =  ['okay','fine','neutral','alright','average','balanced','standard','common','moderate','normal',':pensive_face:',':crying_face:',':disappointed_face:',':worried_face:',':angry_face:',':enraged_face:',':slightly_frowning_face:',':frowning_face:',':persevering_face:']
    negative =  ['unhappy','frustrated','irritated','stressed','annoyed','displeased',':crying_face:','upset','angry','disappointed','sad',':neutral_face:',':expressionless_face:',':face_without_mouth:',':confused_face:',':smirking_face:',':unamused_face:',':confounded_face:',':grimacing_face:',':relieved_face:']

    positive_count = 0
    negative_count = 0
    neutral_count = 0


    for word in review_list:
        if word in positive:
            positive_count += 1
        elif word in negative:
            negative_count += 1
        elif word in neutral:
            neutral_count += 1
        
    sentiment = 0
    if positive_count > negative_count and positive_count > neutral_count:
        sentiment = 'Positive'
    elif negative_count > positive_count and negative_count > neutral_count:
        sentiment = 'Negative'
    elif neutral_count > positive_count and neutral_count > negative_count:
        sentiment = 'Neutral'
    else:
        sentiment = 'Not analyzed'
    return f'Sentiment : {sentiment}'

print(sentiment('I received great news today! 🌟 Excited for the wonderful opportunities ahead! 😃✨'))
print(sentiment('I bought a new gadget, but it turned out to be faulty. 😞 Disappointed with the product quality. '))
print(sentiment("I purchased the product, but it didn't meet my expectations. 😕 Disappointed with the performance and quality."))