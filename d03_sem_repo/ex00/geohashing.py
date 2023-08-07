
import sys, antigravity

def calcGeoHash():
    antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), str(sys.argv[2]).encode('utf-8'))

if __name__ == '__main__':
    if (len(sys.argv) == 4):
        try:
            calcGeoHash()
        except Exception as e:
            print("Description error:", str(e))
    else:
        print('You must provide exactly three argument.')
        