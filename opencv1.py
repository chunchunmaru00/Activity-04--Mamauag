import cv2

def menu():
    filepath = "vi.jpg"

    x = """
        I have provided an image for you :)
        Do you wish to use a different one?
        Please Press...
        [1] To use provided image
        [2] To use your own image """
    print(x)
    input = int(input("Input here: "))
    
    if input == 1:
        input = int(input("[1] Color \n[2] Grayscale \n[3] Unchanged \nRead image as: "))
        if input == 1:
            image = cv2.imread(filepath, 1)
            cv2.imshow("Vi Colored", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        elif input == 2:
            image = cv2.imread(filepath, 0)
            cv2.imshow("Vi Grayscale", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        else:
            image = cv2.imread(filepath, -1)
            cv2.imshow("Vi Unchanged", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        
    elif input1 == 2:
        filepath1 = input("Please Enter Complete and Correct Filepath of your Image:")
        input1 = int(input("[1] Color \n[2] Grayscale \n[3] Unchanged \nWhat you want your image as: "))
        if input1 == 1:
            image = cv2.imread(filepath1, 1)
            cv2.imshow("Image in Color", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        elif input1 == 2:
            image = cv2.imread(filepath1, 0)
            cv2.imshow("Image in Grayscale", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        else:
            image = cv2.imread(filepath1, -1)
            cv2.imshow("Image Unchanged", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
    else:
        print("Please choose between 1 and 2 only, Thank you")
        menu()