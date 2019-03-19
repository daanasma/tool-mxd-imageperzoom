import arcpy
import os
import time
from config import *

def create_output_folder_now(rootdir, outputfoldername):
    """
    - Creates a general outputfolder if it doesn't exist
    - Creates a timestamped specific outputfolder for this analysis.
    :param str rootdir: the root directory of the outputfolder
    :param str outputfoldername: the name of the general outputfolder
    :return str: path to the analysis-specific timestamped outputfolder
    """
    __outputfolder = os.path.join(rootdir, outputfoldername)
    if not os.path.exists(__outputfolder):
        os.makedirs(outputfoldername)
        print('Created general output folder')
    t = time.time()
    timestr = time.strftime("%Y_%m_%d__%Hu%M_%S", time.gmtime(t))
    specific_outputfolder =  os.path.join(__outputfolder, timestr)
    os.makedirs(specific_outputfolder)
    print('Generated specific output folder: {}'.format(specific_outputfolder))
    return specific_outputfolder

def setup_map_document(path_to_map):
    """
    Initializes the MapDocument and DataFrame objects

    :param str path_to_map: the path to the map that needs to be handled
    :return:
    """
    mxd = arcpy.mapping.MapDocument(path_to_map)
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    print('Finished initializing mapdocument and dataframe')
    return mxd, df

def change_df_scale(df, scale):
    """
    Changes the scale level of a dataframe
    :param DataFrame df: the dataframe that should be zoomed
    :param int scale: the scale to the map needs to zoom
    :return: None
    """
    init_scale = df.scale
    df.scale = int(scale)
    print('Updated scale from {} to {}'.format(init_scale, df.scale))

def change_df_position(df, position):
    """
    Changes the position of the dataframe
    :param DataFrame df: the dataframe that should be panned
    :param dict position: the position to which the dataframe should be panned
    :return: None
    """
    print('DF position (orig): {}, {}'.format(df.elementPositionX, df.elementPositionY))
    x = int(position.get('x'))
    y = int(position.get('y'))
    newExt = arcpy.Extent(x - 100, y - 100, x + 100, y + 100)
    df.panToExtent(newExt)
    print('DF position (updated): {})'.format(df.extent))



if __name__ == '__main__':
    output_dir =create_output_folder_now(maindir, output_folder_name)
    mxd, df = setup_map_document(src_map)
    for location in locations:
        print('Starting {}'.format(location.get('name')))
        for scale in scales:
            change_df_scale(df, scale)
            change_df_position(df, location.get('location'))
            output_file = os.path.join(output_dir, '{}_{}.jpg'.format(location.get('name'), scale))
            arcpy.mapping.ExportToJPEG(mxd, output_file,df)
            print ('Exported img: {}'.format(output_file))

    print('Finished. Go Fish.')