class Review :
    Rating_number = 0
    all = []
    def __init__(self,customer,rating) :
        self.customer = customer
        self.Rating_number= rating
        Review.Rating_number +=1
        Review.all.append(self)
    


review_1= Review(1)
return Review
    