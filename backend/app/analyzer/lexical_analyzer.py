class JWTLexer:

    def __init__(self):

        self.b_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_')
        self.d_chars = set('.')

        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'qe'}

        self.start_state = 'q0'
        self.final_state = {'q5'}

        self.transitions = {
            'q0': {'b': 'q1', 'd': 'qe'},
            'q1': {'b': 'q1', 'd': 'q2'},
            'q2': {'b': 'q3', 'd': 'qe'},
            'q3': {'b': 'q3', 'd': 'q4'},
            'q4': {'b': 'q5', 'd': 'qe'},
            'q5': {'b': 'q5', 'd': 'qe'},
            'qe': {'b': 'qe', 'd': 'qe'},
        }

    def get_char_class(self, char):
        if char in self.b_chars:
            return 'b'
        elif char in self.d_chars:
            return 'd'
        else:
            return 'other'

    def analyze(self, token):

        current_state = self.start_state

        for char in token:

            char_class = self.get_char_class(char)

            if char_class == 'other':
                current_state = 'qe'
                break

            current_state = self.transitions[current_state][char_class]

        isAccepted = current_state in self.final_state

        if isAccepted:
            tokens = token.split('.')
            return {
                'valid': True, 
                'tokens': tokens,
                'header': tokens[0] if len(tokens) > 0 else '',
                'payload': tokens[1] if len(tokens) > 1 else '',
                'signature': tokens[2] if len(tokens) > 2 else ''
            }
        else:
            return {
                'valid': False, 
                'tokens': [],
                'error': 'Invalid JWT format'
            }

