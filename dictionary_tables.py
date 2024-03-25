# Without intonation
greek_to_greeklish = {'α': ['a'], 'ε': ['e'], 'η': ['h', 'i'], 'ι': ['i'], 'ο': ['o'], 'υ': ['u', 'y', 'i'],
                    'ω': ['w', 'o'], 'β': ['b', 'v'], 'γ': ['g'], 'δ': ['d'], 'ζ': ['z'], 'θ': ['th', 'u'],
                    'κ': ['k'], 'λ': ['l'], 'μ': ['m'], 'ν': ['n'], 'ξ': ['ks', 'x'], 'π': ['p'],
                    'ρ': ['r'], 'σ': ['s'], 'ς': ['s'], 'τ': ['t'], 'χ': ['x', 'h'], 'φ': ['f'], 'ψ': ['ps'],

                    'Α': ['A'], 'Ε': ['E'], 'Η': ['H', 'I'], 'Ι': ['I'], 'Ο': ['O'], 'Υ': ['Y', 'I'],
                    'Ω': ['W', 'O'], 'Β': ['B', 'V'], 'Γ': ['G'], 'Δ': ['D'], 'Ζ': ['Z'],
                    'Θ': ['Th', 'U', 'Q'], 'Κ': ['K'], 'Λ': ['L'], 'Μ': ['M'], 'Ν': ['N'], 'Ξ': ['Ks', 'X'],
                    'Π': ['P'], 'Ρ': ['R'], 'Σ': ['S'], 'Τ': ['T'], 'Χ': ['X', 'H'], 'Φ': ['F'], 'Ψ': ['P'],

                    'ει': ['ei', 'i'], 'οι': ['oi', 'i'], 'ου': ['ou', 'u'], 'αι': ['ai', 'e'],
                    'υι': ['ui', 'i'], 'μπ': ['mp', 'b'], 'ντ': ['nt', 'd'],

                    'Ει': ['Ei', 'I'], 'Οι': ['Oi', 'I'], 'Ου': ['Ou', 'U'], 'Αι': ['Ai', 'E'],
                    'Υι': ['Yi', 'I'], 'Μπ': ['Mp', 'B'], 'Ντ': ['Nt', 'D']}

greeklish_to_greek = {'A': ['Α'], 'Ai': ['Αι'], 'B': ['Β', 'Μπ'], 'D': ['Δ', 'Ντ'], 'E': ['Ε', 'Αι'], 'Ei': ['Ει'],
                      'F': ['Φ'], 'G': ['Γ'], 'H': ['Η', 'Χ'], 'I': ['Η', 'Ι', 'Υ', 'Ει', 'Οι', 'Υι'], 'K': ['Κ'],
                      'Ks': ['Ξ'], 'L': ['Λ'], 'M': ['Μ'], 'Mp': ['Μπ'], 'N': ['Ν'], 'Nt': ['Ντ'], 'O': ['Ο', 'Ω'],
                      'Oi': ['Οι'], 'Ou': ['Ου'], 'P': ['Π', 'Ψ'], 'Q': ['Θ'], 'R': ['Ρ'], 'S': ['Σ'], 'T': ['Τ'],
                      'Th': ['Θ'], 'U': ['Θ', 'Ου', 'Y'], 'V': ['Β'], 'W': ['Ω'], 'X': ['Ξ', 'Χ'], 'Y': ['Υ'], 'Yi': ['Υι'],
                      'Z': ['Ζ'], 'a': ['α'], 'ai': ['αι'], 'b': ['β', 'μπ'], 'd': ['δ', 'ντ'],
                      'e': ['ε', 'αι'], 'ei': ['ει'], 'f': ['φ'], 'g': ['γ'], 'h': ['η', 'χ'],
                      'i': ['η', 'ι', 'υ', 'ει', 'οι', 'υι'], 'k': ['κ'], 'ks': ['ξ'], 'l': ['λ'], 'm': ['μ'],
                      'mp': ['μπ'], 'n': ['ν'], 'nt': ['ντ'], 'o': ['ο', 'ω'], 'oi': ['οι'], 'ou': ['ου'], 'p': ['π'],
                      'ps': ['ψ'], 'r': ['ρ'], 's': ['σ', 'ς'], 't': ['τ'], 'th': ['θ'], 'u': ['υ', 'θ', 'ου'],
                      'ui': ['υι'], 'v': ['β'], 'w': ['ω'], 'x': ['ξ', 'χ'], 'y': ['υ'], 'z': ['ζ']}

# With intonation
greek_to_greeklish_intonated = {'α': ['a'], 'ε': ['e'], 'η': ['h', 'i'], 'ι': ['i'], 'ο': ['o'], 'υ': ['u', 'y', 'i'],
                                'ω': ['w', 'o'], 'β': ['b', 'v'], 'γ': ['g'], 'δ': ['d'], 'ζ': ['z'], 'θ': ['th', 'u'],
                                'κ': ['k'], 'λ': ['l'], 'μ': ['m'], 'ν': ['n'], 'ξ': ['ks', 'x'], 'π': ['p'],
                                'ρ': ['r'], 'σ': ['s'], 'ς': ['s'], 'τ': ['t'], 'φ': ['f'], 'χ': ['x', 'h'], 'ψ': ['ps'],

                                'Α': ['A'], 'Ε': ['E'], 'Η': ['H', 'I'], 'Ι': ['I'], 'Ο': ['O'], 'Υ': ['Y', 'U', 'I'],
                                'Ω': ['W', 'O'], 'Β': ['B', 'V'], 'Γ': ['G'], 'Δ': ['D'], 'Ζ': ['Z'],
                                'Θ': ['Th', 'U', 'Q'], 'Κ': ['K'], 'Λ': ['L'], 'Μ': ['M'], 'Ν': ['N'], 'Ξ': ['Ks', 'X'],
                                'Π': ['P'], 'Ρ': ['R'], 'Σ': ['S'], 'Τ': ['T'], 'Χ': ['X', 'H'], 'Φ': ['F'], 'Ψ': ['P'],

                                'ει': ['ei', 'i'], 'οι': ['oi', 'i'], 'ου': ['ou', 'u'], 'αι': ['ai', 'e'],
                                'υι': ['ui', 'i'], 'μπ': ['mp', 'b'], 'ντ': ['nt', 'd'],

                                'Ει': ['Ei', 'I'], 'Οι': ['Oi', 'I'], 'Ου': ['Ou', 'U'], 'Αι': ['Ai', 'E'],
                                'Υι': ['Yi', 'I'], 'Μπ': ['Mp', 'B'], 'Ντ': ['Nt', 'D'],

                                'ά': ['a'], 'έ': ['e'], 'ή': ['h', 'i'], 'ί': ['i'], 'ό': ['o'], 'ύ': ['u', 'y', 'i'],
                                'ώ': ['w', 'o'],
                                'Ά': ['A'], 'Έ': ['E'], 'Ή': ['H', 'I'], 'Ί': ['I'], 'Ό': ['O'], 'Ύ': ['Y', 'U', 'I'],
                                'Ώ': ['W', 'O'],

                                'εί': ['ei', 'i'], 'οί': ['oi', 'i'], 'ού': ['ou', 'u'], 'αί': ['ai', 'e'],
                                'υί': ['ui', 'i'],
                                'Εί': ['Ei', 'I'], 'Οί': ['Oi', 'I'], 'Ού': ['Ou', 'U'], 'Αί': ['Ai', 'E'],
                                'Υί': ['Yi', 'I'],
                                }


greeklish_to_greek_intonated = {'A': ['Α', 'Ά'], 'Ai': ['Αι', 'Αί'], 'B': ['Β', 'Μπ'], 'D': ['Δ', 'Ντ'],
                                'E': ['Ε', 'Αι', 'Έ', 'Αί'], 'Ei': ['Ει', 'Εί'], 'F': ['Φ'], 'G': ['Γ'],
                                'H': ['Η', 'Χ', 'Ή'],
                                'I': ['Η', 'Ι', 'Υ', 'Ει', 'Οι', 'Υι', 'Ή', 'Ί', 'Ύ', 'Εί', 'Οί', 'Υί'],
                                'K': ['Κ'], 'Ks': ['Ξ'], 'L': ['Λ'], 'M': ['Μ'], 'Mp': ['Μπ'], 'N': ['Ν'],
                                'Nt': ['Ντ'], 'O': ['Ο', 'Ω', 'Ό', 'Ώ'], 'Oi': ['Οι', 'Οί'], 'Ou': ['Ου', 'Ού'],
                                'P': ['Π', 'Ψ'], 'Q': ['Θ'], 'R': ['Ρ'], 'S': ['Σ'], 'T': ['Τ'], 'Th': ['Θ'],
                                'U': ['Θ', 'Ου', 'Ού', 'Υ', 'Ύ'], 'V': ['Β'], 'W': ['Ω', 'Ώ'], 'X': ['Ξ', 'Χ'], 'Y': ['Υ', 'Ύ'],
                                'Yi': ['Υι', 'Υί'], 'Z': ['Ζ'], 'a': ['α', 'ά'], 'ai': ['αι', 'αί'], 'b': ['β', 'μπ'],
                                'd': ['δ', 'ντ'], 'e': ['ε', 'αι', 'έ', 'αί'], 'ei': ['ει', 'εί'], 'f': ['φ'],
                                'g': ['γ'], 'h': ['η', 'χ', 'ή'],
                                'i': ['η', 'ι', 'υ', 'ει', 'οι', 'υι', 'ή', 'ί', 'ύ', 'εί', 'οί', 'υί'],
                                'k': ['κ'], 'ks': ['ξ'], 'l': ['λ'], 'm': ['μ'], 'mp': ['μπ'], 'n': ['ν'],
                                'nt': ['ντ'], 'o': ['ο', 'ω', 'ό', 'ώ'], 'oi': ['οι', 'οί'], 'ou': ['ου', 'ού'],
                                'p': ['π'], 'ps': ['ψ'], 'r': ['ρ'], 's': ['σ', 'ς'], 't': ['τ'], 'th': ['θ'],
                                'u': ['υ', 'θ', 'ου', 'ύ', 'ού'], 'ui': ['υι', 'υί'], 'v': ['β'], 'w': ['ω', 'ώ'],
                                'x': ['ξ', 'χ'], 'y': ['υ', 'ύ'], 'z': ['ζ']}

