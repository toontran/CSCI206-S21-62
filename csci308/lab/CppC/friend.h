#ifndef FRIEND_H
#define FRIEND_H

// You will need to edit this file

class RodeoClown  {
friend class Bull;
public:
  void laugh();
  void gallop();
private: void dance(); // KEEP THIS PRIVATE
};

class Bull {
friend class Spectators;
public:
  void charge(RodeoClown * clown);
private: bool excited; // KEEP THIS PRIVATE
};

class Spectators{
public:
  void applaude(Bull * bull);
};

#endif
