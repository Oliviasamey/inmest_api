package Subscription;

import transaction.PaymentInterface;

public class PremiumSub extends FreemiumSub {
    private PaymentInterface paymentInterface;

    public PremiumSub(SubEnum duration, int allowed){
        super(duration, allowed);
        this.paymentInterface = paymentInterface;
    }
    
}
