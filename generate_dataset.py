##This file contains a class that takes images folder as input and produces augmented images based on the settings provided.

import Augmentor

class ImageAugmentor():
        
    def createPipeline(self,folder_name):
        pipeline=Augmentor.Pipeline(folder_name)
        return pipeline
        
    
    def random_rotation(self,pipeline_object,probability, max_left_rotation, max_right_rotation,number_of_samples):
        pipeline_object.rotate(probability, max_left_rotation, max_right_rotation)
        pipeline_object.rotate180(probability)
        pipeline_object.rotate90(probability)
        pipeline_object.rotate270(probability)
        pipeline_object.sample(number_of_samples)

    def random_zoom(self,pipeline_object, probability,min_factor, max_factor,number_of_samples):
        pipeline_object.zoom(probability,min_factor, max_factor)
        pipeline_object.sample(number_of_samples)
    


def main():
    folder_name=input("Enter the images folder: ")
    number_of_samples=int(input("Enter the number of images to generate: "))
    augmentor=ImageAugmentor()
    augmentor_pipeline=augmentor.createPipeline(folder_name)
    augmentor.random_rotation(augmentor_pipeline,0.5,1,1.5,number_of_samples)



if __name__=="__main__":
    main()









    







