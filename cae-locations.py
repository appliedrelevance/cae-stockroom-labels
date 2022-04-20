# Generate a CSV File containing inventory locations for the
# CAE Healthcare facility in Sarasota.
#

import csv

with open('locations-a.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, dialect='excel')
    head = ['Aisle', 'Level', 'Position', 'Location', 'Description']
    csvwriter.writerow(head)
    # Aisle        Level (shelves)   Position (right-to-left on shelves on the front side)
    # 02->14     01->09               01->24
    # Example: 03 04 02
    for aisle in range(2, 15):
        strAisle = str(aisle)
        strAisle = strAisle.rjust(2, '0')  # 02, 03, 04...
        for level in range(1, 10):
            strLevel = str(level)
            strLevel = strLevel.rjust(2, '0')  # 01, 02...
            for position in range(1, 25):
                strPosition = str(position)
                strPosition = strPosition.rjust(2, '0')
                row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                       'Stockroom Floor - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
                csvwriter.writerow(row)
with open('locations-b.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, dialect='excel')
    head = ['Aisle', 'Level', 'Position', 'Location', 'Description']
    csvwriter.writerow(head)
    # Aria product specific shelves:
    # ARIA        01->09                01->07
    # Example: ARIA 06 05
    strAisle = 'ARIA'
    for level in range(1, 10):
        strLevel = str(level)
        strLevel = strLevel.rjust(2, '0')  # 01, 02...
        for position in range(1, 8):
            strPosition = str(position)
            strPosition = strPosition.rjust(2, '0')
            row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                   'Aria product specific - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
            csvwriter.writerow(row)
    # Blue Phantom specific shelves:
    # BP            01->04                01->09
    # Example: BP 04 02
    strAisle = 'BP'
    for level in range(1, 5):
        strLevel = str(level)
        strLevel = strLevel.rjust(2, '0')  # 01, 02...
        for position in range(1, 10):
            strPosition = str(position)
            strPosition = strPosition.rjust(2, '0')
            row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                   'Blue Phantom specific - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
            csvwriter.writerow(row)

    # Customer Service (this is Aisle 1):
    # "back side"
    # CS            A1->A10             A1->F1
    # for sections ^-- A, B, C, F
    # "front side"
    # Example: CS C5 F1
    # CS            E1->E10             A1->F1
    # for sections ^-- E, G, J, H
    # Example: CS G3 B1
    strAisle = 'CS'
    for strSection in ['A', 'B', 'C', 'F']:
        for level in range(1, 11):
            strLevel = strSection + str(level)
            for strPosition in ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']:
                row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                       'Customer Service  - Back Side - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
                csvwriter.writerow(row)
    for strSection in ['E', 'G', 'J', 'H']:
        for level in range(1, 11):
            strLevel = strSection + str(level)
            for strPosition in ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']:
                row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                       'Customer Service - Front Side - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
                csvwriter.writerow(row)
    # End caps:
    # "front side"
    # 01->09      HW                      01->09
    # Example: 04 HW 05
    # "back side"
    # 01->09       BK ENDCAP       1-9 (single digits)
    # Example: 04 BK ENDCAP 3
    for aisle in range(1, 10):
        strAisle = str(aisle)
        strAisle = strAisle.rjust(2, '0')  # 02, 03, 04...
        strLevel = 'HW'
        for position in range(1, 10):
            strPosition = str(position)
            strPosition = strPosition.rjust(2, '0')
            row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                   'End Cap - Front Side - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
            csvwriter.writerow(row)
    for aisle in range(1, 10):
        strAisle = str(aisle)
        strAisle = strAisle.rjust(2, '0')  # 02, 03, 04...
        strLevel = 'BK ENDCAP'
        for position in range(1, 10):
            strPosition = str(position)
            row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                   'End Cap - BAck Side - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
            csvwriter.writerow(row)
    # Engineering:
    # ENG           01->09                01->24
    # Example: ENG 02 18
    strAisle = 'ENG'
    for level in range(1, 9):
        strLevel = str(level)
        strLevel = strLevel.rjust(2, '0')  # 01, 02...
        for position in range(1, 19):
            strPosition = str(position)
            strPosition = strPosition.rjust(2, '0')
            row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
                   'Engineering - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
            csvwriter.writerow(row)
    # Engineering end cap:
    # ENG           HW                      01->09
    # Example: ENG HW 04
    strAisle = 'ENG'
    strLevel = 'HW'
    for position in range(1, 10):
        strPosition = str(position)
        strPosition = strPosition.rjust(2, '0')
        row = [strAisle, strLevel, strPosition, strAisle + ' ' + strLevel + ' ' + strPosition,
               'Engineering endcap - Aisle ' + strAisle + ' Level ' + strLevel + ' Position ' + strPosition]
        csvwriter.writerow(row)
