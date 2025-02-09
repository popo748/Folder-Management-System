import { defineStore } from "pinia";
import { useApi } from "../composables/useApi";

interface Folder {
  id?: number;
  title: string;
  
}

export const useFolderStore = defineStore("folderStore", {
  state: () => ({
    folders: [] as Folder[],
  }),
  actions: {
    async fetchFolders(): Promise<Folder[]> {
      try {
        const api = useApi();
        const response = await api.get("/folders");
        this.folders = response.data;
        return this.folders;
      } catch (error) {
        console.error("Error fetching folders:", error);
        throw error;
      }
    },
    async saveFolder(folder: Folder): Promise<void> {
      try {
        const api = useApi();
        if (folder.id) {
          await api.put(`/folders/${folder.id}`, folder);
        } else {
          await api.post("/folders/create_folder", folder);
        }
      } catch (error) {
        console.error("Error saving folder:", error);
        throw error;
      }
    },
    async deleteFolder(folderId: number): Promise<void> {
      try {
        const api = useApi();
        await api.delete(`/folders/${folderId}`);
      } catch (error) {
        console.error("Error deleting folder:", error);
        throw error;
      }
    },
  },
});