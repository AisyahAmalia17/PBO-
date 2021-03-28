def pure_func(List):
      
    New_List = []
      
    for i in List:
        New_List.append(i**4)
          
    return New_List

A = [27, 9, 4, 16]
B = pure_func(A)
  
print("Angka awal: ", A)
print("Hasil:", B)