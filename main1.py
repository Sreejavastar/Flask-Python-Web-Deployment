import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        # print('Sorry could not understand..')
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','are', 'you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])


    # Longer responses
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_ADVICE0, ['can', 'help', 'me'], required_words=['help'])
    response(long.R_ADVICE1, ['provide', 'feedback', 'sources', 'assignment'], required_words=['provide', 'feedback', 'assignment'])
    response(long.R_ADVICE2, ['improve', 'clarity', 'writing'], required_words=['improve', 'clarity'])
    response(long.R_ADVICE3, ['specific', 'writing', 'focus', 'improving'], required_words=['specific', 'writing', 'improving'])
    response(long.R_ADVICE4, ['recommend', 'resources', 'tools'], required_words=['recommend', 'resources'])
    response(long.R_ADVICE5, ['common', 'mistakes'], required_words=['common', 'mistakes'])
    response(long.R_ADVICE6, ['improve', 'overall', 'structure', 'organization'], required_words=['structure'])
    response(long.R_ADVICE7, ['provide', 'suggestions', 'argument'], required_words=['suggestions', 'argument'])
    response(long.R_ADVICE8, ['improve', 'transitions', 'between', 'paragraphs'], required_words=['transitions','paragraphs'])
    response(long.R_ADVICE9, ['give', 'answers'], required_words=['give', 'answers'])
    response(long.R_ADVICE10, ['think', 'of', 'course', 'material'], required_words=['course', 'material'])
    response(long.R_ADVICE11, ['think', 'of', 'instructor'], required_words=['instructor'])
    response(long.R_ADVICE12, ['pace', 'of', 'course'], required_words=['pace', 'course'])
    response(long.R_ADVICE13, ['course', 'workload', 'manageable'], required_words=['course', 'workload'])
    response(long.R_ADVICE14, ['find', 'course', 'assignments', 'helpful'], required_words=['course', 'assignments', 'helpful'])
    response(long.R_ADVICE15, ['technical', 'difficulties', 'issues', 'course', 'platform'], required_words=['technical', 'difficulties'])
    response(long.R_ADVICE16, ['How', 'course', 'improved'], required_words=['how', 'course', 'improved'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))