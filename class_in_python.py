class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles): # this is method
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter() # define the name of class
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"



class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"
