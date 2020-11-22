QMAKE_CXXFLAGS_DEBUG += -fno-inline -fno-inline-functions -fno-inline-small-functions -O0

QMAKE_CXXFLAGS_RELEASE += -msse2 -Ofast
QMAKE_LFLAGS_RELEASE += -flto

LIBS += -lstdc++fs -lpthread -lrt
