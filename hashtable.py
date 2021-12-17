#  Class: ChainingHashTable
#  Uses list with in the table
class ChainingHashTable:
    #  Starts as table is empty
    #  O(N) -- Holds 10 buckets
    def __init__(self, holds=10):
        self.root = []
        for i in range(holds):
            self.root.append([])

    #  Additional function
    #  O(N) -- List all package items to find the size of list
    def list_items(self):
        count = 0
        for i in range(10):
            bucket_items = self.root[i]
            for item in bucket_items:
                count += 1
        return count

    #  O(1) -- Insert a new item into the hash table - O(1)
    def insert(self, key, item):
        # Get bucket ID from hash function
        bucket = self.bucket_hash(key)
        # Store the item in that bucket
        self.root[bucket].append(item)

    #  O(LOG N) -- Searches for an item, and return the item if it is found
    def search(self, key):
        # Find id from function
        bucket = self.bucket_hash(key)
        bucket_items = self.root[bucket]
        # Search through all package objects and find the package id
        for item in bucket_items:
            if item.package_id == key:
                # Return the package id when indexed
                index = bucket_items.index(item)
                return bucket_items[index]
        else:
            return None

    #  O(log n) -- Find package id and remove package information
    def remove(self, key):
        # Find Id from function
        bucket = self.bucket_hash(key)
        bucket_items = self.root[bucket]
        for item in bucket_items:
            # If the id is package id is found, remove the package info
            if item.package_id == key:
                bucket_items.remove(item)

    #  O(1) -- Return package id as the item
    def bucket_hash(self, item):
        return item % len(self.root)
