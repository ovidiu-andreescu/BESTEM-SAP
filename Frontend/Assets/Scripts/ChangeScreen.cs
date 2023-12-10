using UnityEngine;
using UnityEngine.SceneManagement;

public class SchimbareScene : MonoBehaviour
{
    // Funcție pentru a schimba scenele în funcție de parametrul primit
    public void SchimbaScene(int indexScene)
    {
        SceneManager.LoadScene(indexScene);
    }
}
