
def transaction_confirmation(transaction):

    transaction.confirm()

    '''
    This method should be called when callback or confirmation about transaction is received from a partner
    If partner API is without auto callback, then trans status check should be scheduled as task
    '''
    return None