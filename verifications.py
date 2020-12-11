def println(lst):
    '''generate orders to validate model in gnu-prolog
    '''
    inside = ', '.join(lst)
    order = f'L = [{inside}].'
    print(order)
    # print('lpinmuebles(L).')
    # print(f'gprolog  --consult-file inmueble.pl --query-goal lpinmuebles([{inside}])')
    return order

# all possible features
leaves = [
    'F0',
    'RF1', 'RF2', 'RF3', 'RF4', 'RF5', 'RF6', 'RF7', 'RF8', 'RF9', 
    'RF11', 'RF12', 
    'RF21', 'RF22', 'RF23', 'RF24', 
    'RF31', 'RF32', 'RF33', 'RF34', 'RF35', 'RF36', 'RF37', 
    'RF41', 'RF42', 'RF43', 
    'RF51', 'RF52', 'RF53', 
    'RF61', 'RF62', 'RF63', 'RF64', 
    'RF71', 'RF72', 'RF73', 
    'RF81', 'RF91', 'RF92'
    ]

# features set as variable (can be 0 or 1)
variable_leaves = [
    'RF12', 'RF22', 'RF24', 'RF31', 'RF32', 
    'RF33', 'RF34', 'RF35', 'RF36', 'RF37',
    'RF41', 'RF43', 'RF5', 'RF51', 'RF52', 'RF53',
    'RF63', 'RF7', 'RF72', 'RF73', 'RF8', 'RF81',
    'RF92'
    ]


def validation_code_generators():
    '''Generate code lines to be introduced in GNU-Prolog 
    interactive teminal in order to make different kind 
    of validations once loaded inmueble.pl file
    '''
    # validate if model itself has any result
    general_validation = ['_' for a in leaves]
    println(general_validation)
    # validata if variable features are really variables
    for vr in variable_leaves:
        # validate if there are responses for false and true for a feature
        # that is supposed to be variable
        true_validation = list(map(lambda x: '_' if vr != x else '1', leaves))
        false_validation = list(map(lambda x: '_' if vr != x else '0', leaves))
        print(vr)
        println(true_validation)
        println(false_validation)


def validate_model_results():
    # load result file
    with open('oth.txt', 'r') as fl:
        rw = fl.read()
        lns = [a.strip()[5:-1] for a in rw.split('\n') if len(a.strip()) > 2 and a.startswith('L')]
        # delete set deffinition
        lns.pop(0)
        print('false product model, empty or single product' if len(lns) < 1 else 'true product model')
        print('possible products: ', len(lns))
    
    # make lns lists to be used
    product_line_setups = []
    for pr in lns:
        product_line_setups.append([int(a[0]) for a in pr.split(',')])
    # check all files to figure out if variables are variables
    # and constants are constants
    constant_leaves = []
    for ft in leaves:
        if ft in variable_leaves:
            zero_val = None
            one_val = None
            indx = leaves.index(ft)
            for stp in product_line_setups:
                if stp[indx] == 1:
                    one_val = True
                else:
                    zero_val = True
                if all([zero_val, one_val]):
                    print(f'{ft} designed as variable is variable')
                    break
            if not all([zero_val, one_val]):
                print(f'{ft} designed as variable is not variable')

        else:
            constant_leaves.append(ft)
            one_val = None
    print('constant features: ', constant_leaves)



if __name__ == "__main__":
    somestuff()